# Updated from pyscriptv4.py: 
#     (1) added encoding so that user can still type in non-ENG characters under editURL()
#     (2) when stopwatch is running, a text 'tictoc' will blink to indicate function is on
#     (3) Help menu has been revised by adding a. Show Information b. Show Instruction c. Show Full Code

#1. Libraries
from pathlib import Path
from tkinter import messagebox, Menu
import datetime
import os
import subprocess
import tempfile
import threading
import time
import tkinter as tk
import webbrowser
    
#2. Functions
## Variables
alarm_thread = None
sum_min_list = []
sum_sec_list = []

## Function to define subwindow's attributes
def sub_window(sub_window_title):
    global sub_window_global
    sub_window_global = tk.Toplevel(root)
    sub_window_global.title(sub_window_title)

    main_x = root.winfo_x()
    main_y = root.winfo_y()

    sub_window_x = main_x + 195
    sub_window_y = main_y
    sub_window_global.geometry("+{}+{}".format(sub_window_x, sub_window_y))

## Function to alert before closing the app (purpose: avoid accidental closure)
def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        global running
        running = False
        root.destroy()

## Function for "Calculate Lunch" button(purpose: calculate)
def lunch_cal(entry_lstart, entry_lend, l_result_label):
    try:
        lstime_str = entry_lstart.get()
        s_hour, s_minute = map(int, lstime_str.split(":"))
        #allow user to type 1:15 instead of 13:15
        if s_hour < 7:
            s_hour +=12
            
        letime_str = entry_lend.get()
        e_hour, e_minute = map(int, letime_str.split(":"))
        #allow user to type 1:15 instead of 13:15
        if e_hour < 7:
            e_hour +=12
        
        l_total_minute = (e_hour*60 + e_minute)- (s_hour*60 + s_minute)
        l_result_label.config(text=f" Total {l_total_minute:02d} Minutes")
        
        entry2.delete(0, tk.END)
        entry2.insert(0, str(l_total_minute))
    except ValueError:
        messagebox.showinfo("Alert", "[ERROR] Enter Time Correctly!")  

## Function for "Calculate Lunch" button(purpose: show window)
def lunch_submit():
    global sub_window_global 
    sub_window("Calculate Lunch")
    sub_window_global.geometry("180x150")

    label_lstart = tk.Label(sub_window_global, text="Started (HH:MM)")
    label_lstart.pack()

    entry_lstart = tk.Entry(sub_window_global)
    entry_lstart.pack()

    label_lend = tk.Label(sub_window_global, text="Finished (HH:MM)")
    label_lend.pack()

    entry_lend = tk.Entry(sub_window_global)
    entry_lend.pack()

    lunch_gl_label = tk.Label(sub_window_global, text="Hit Enter to Calculate Time", fg="gray")
    lunch_gl_label.pack()

    l_result_label = tk.Label(sub_window_global, text="", fg="#009900")
    l_result_label.pack()
    entry_lend.bind("<Return>", lambda event: lunch_cal(entry_lstart, entry_lend, l_result_label))
    
## Function for "Set Alarm" button(purpose: calculate)
def punch_calculator():
    try:
        time_str = entry1.get()
        hour, minute = map(int, time_str.split(":"))
        lunch_minute = int(entry2.get())
        total_minute = hour*60 + minute + 8*60+ lunch_minute
        hour = total_minute // 60
        minute = total_minute % 60
        result_label.config(text=f"Record Out at {hour:02d}:{minute:02d}")
        messagebox.showinfo("Confirmation", "Alarm set!")
    except ValueError:
        messagebox.showinfo("Alert", "[ERROR] Enter Time Correctly!")
        return

## Function for "Set Alarm" button(purpose: validate entries)
def set_alarm():
    global alarm_thread

    if entry1.get() == "" or entry2.get() == "":
        messagebox.showinfo("Alert", "[ERROR] Missing Time!")
        return
    else:
        if alarm_thread and alarm_thread.is_alive():
            global running
            running = False
            alarm_thread.join()
            punch_calculator()
        else:
            punch_calculator()

    set_time = result_label["text"][13:]
    alarm_thread = threading.Thread(target=check_current_time, args=(set_time,))
    alarm_thread.start()

## Function for "Set Alarm" button(purpose: ring alarm)
def check_current_time(set_time):
    global running  #to prevent from running even after closure
    running = True
    while running:
        now = datetime.datetime.now()
        current_time = f"{now.hour:02d}:{now.minute:02d}"
        if current_time == set_time:
            cmd = """
                   do shell script "afplay /System/Library/Sounds/Funk.aiff"
                   display dialog ¬
                   "Time to Go Home!" 
                        """
            result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
            os.system("open -a 'Time'")

            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            result_label.config(text="")

            return result.stdout
            break
        time.sleep(1)

## Function to alert before closing stopwatch
def close_window(sub_window_global):
    result = messagebox.askquestion("Confirmation", "Are you sure you want to close?")
    if result == "yes":
        sub_window_global.destroy()
    
# Function for "Stopwatch" button
def stopwatch():
    global sub_window_global
    sub_window("Stopwatch")

    sst1 = ""
    sst2 = ""
    label_row = 2  # Initial row index for label_records

    def stamp_start_time():
        nonlocal sst1
        stamp_start_time = datetime.datetime.now()
        sst1 = stamp_start_time.strftime("%H:%M:%S")
        label_start.config(text=sst1)
        update_indicator()

    def stamp_end_time():
        nonlocal sst2
        stamp_end_time = datetime.datetime.now()
        sst2 = stamp_end_time.strftime("%H:%M:%S")

        try:
            if label_start.cget("text") != "":
                nonlocal label_row  # Access the label_row variable from the outer scope
                sst1_h, sst1_m, sst1_s = map(int, sst1.split(":"))
                sst2_h, sst2_m, sst2_s = map(int, sst2.split(":"))

                if sst2_s > sst1_s:
                    time_diff_s = sst2_s - sst1_s
                    records_m = (sst2_h * 60 + sst2_m) - (sst1_h * 60 + sst1_m)
                else:
                    time_diff_s = sst2_s + 60 - sst1_s
                    records_m = (sst2_h * 60 + sst2_m - 1) - (sst1_h * 60 + sst1_m)

                label_records = tk.Label(sub_window_global, text=f"{sst1} - {sst2} Total {records_m} minutes {time_diff_s} seconds")
                label_records.grid(row=label_row, column=0, columnspan=4)

                label_row += 1  # Increment the row index for the next label_records

                sum_min_list.append(records_m)
                sum_sec_list.append(time_diff_s)

                label_start.config(text="")
                update_indicator()
                
        except Exception as e:
            pass

    def sumup():
        initial_min_stopwatch = sum(sum_min_list)
        additional_min_stopwatch = sum(sum_sec_list) // 60
        total_min_stopwatch = initial_min_stopwatch + additional_min_stopwatch
        total_sec_stopwatch = sum(sum_sec_list) % 60

        label_total_time = tk.Label(
            sub_window_global,
            text=f"Total {total_min_stopwatch} minutes {total_sec_stopwatch} seconds",
            fg="#009900"
        )
        label_total_time.grid(row=label_row, column=0, columnspan=4)

    def reset_start_button():
        label_start.config(text="")
        indicator_label.config(text="")

    def update_indicator():
        indicator_text = "tic" + "toc" * (int(time.time()) % 2 == 0)
        indicator_label.config(text=indicator_text)
        if label_start.cget("text") == "":
            indicator_label.config(text="")
        else:
            sub_window_global.after(1000, update_indicator)

    stopwatch_start_button = tk.Button(sub_window_global, text="Start", command=stamp_start_time)
    stopwatch_start_button.grid(row=0, column=0)

    stopwatch_end_button = tk.Button(sub_window_global, text="End", command=stamp_end_time)
    stopwatch_end_button.grid(row=0, column=1)

    sumup_button = tk.Button(sub_window_global, text="Sum Up", command=sumup)
    sumup_button.grid(row=0, column=2)

    stopwatch_reset_button = tk.Button(sub_window_global, text="Reset", command=reset_start_button)
    stopwatch_reset_button.grid(row=0, column=3)

    label_start = tk.Label(sub_window_global, text=sst1, fg="#009900")
    label_start.grid(row=1, column=0)

    indicator_label = tk.Label(sub_window_global, text="", fg="#009900")
    indicator_label.grid(row=1, column=1)

    sub_window_global.protocol("WM_DELETE_WINDOW", lambda: close_window(sub_window_global))
    sub_window_global.mainloop()
    
## Function for "Open URL" button
def openURL():
    file_path = get_file_path()
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("https://google.com\n")

    with open(file_path, "r", encoding="utf-8") as f:
        urls = f.read().splitlines()

    for url in urls:
        if not url.startswith("https://") and url:
            full_url="https://" + url
        else:
            full_url = url
            
        webbrowser.open_new_tab(full_url)

def editURL():
    global sub_window_global 
    sub_window("Edit URL")
    
    lab_url1 = tk.Label(sub_window_global, text="Your URL(s)")
    lab_url1.pack()

    file_path = get_file_path()
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("https://google.com\n")

    with open(file_path, "r", encoding="utf-8") as f:
        urls = f.read().splitlines()

    num_entries = len(urls)
    entries = []

    for i in range(num_entries):
        entry = tk.Entry(sub_window_global)
        entry.insert(0, urls[i])
        entry.pack()
        entries.append(entry)

    def create_new_field():
        new_entry = tk.Entry(sub_window_global)
        new_entry.pack()
        entries.append(new_entry)
        add_button.pack(side=tk.BOTTOM)

    def save_urls():
        urls = [entry.get() for entry in entries]
        with open(file_path, "w", encoding="utf-8") as f:
            for url in urls:
                f.write(url + "\n")
        sub_window_global.destroy()

    add_button = tk.Button(sub_window_global, text="Add", command=create_new_field)
    add_button.pack(side=tk.BOTTOM)

    sub_window_global.protocol("WM_DELETE_WINDOW", save_urls)

def get_file_path():
    home_dir = str(Path.home())
    file_path = os.path.join(home_dir, "url_list.txt")
    return file_path


#3. Main Window 
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Ops Helper")


#4. Labels and Entries
label1 = tk.Label(root, text="Start Time (HH:MM)")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Lunch Time (MM)")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()    
    
entry2.bind("<Return>", lambda event: set_alarm())

result_label = tk.Label(root, text="", fg="#009900")
result_label.pack()


#5. Buttons
button_lcal = tk.Button(root, width=10, text="Calculate Lunch", command=lunch_submit)
button_lcal.pack()

button1 = tk.Button(root, width=10, text="Set Alarm", command=set_alarm)
button1.pack()

button3 = tk.Button(root, width=10, text="Stopwatch", command=stopwatch)
button3.pack()

button2 = tk.Button(root, width=10, text="Open URL", command=openURL)
button2.pack()

button2_edit = tk.Button(root, width=10, text="Edit URL", command=editURL)
button2_edit.pack()

version_label = tk.Label(root, text="Sylvia-GUI-prj-June2023", fg="gray")
version_label.pack()


#6. Help Menu
def show_help():
    help_text = """
    Added app information here
    """

    help_window = tk.Toplevel(root)
    help_window.title("Help")

    help_label = tk.Label(help_window, text=help_text, padx=10, pady=10, justify='left')
    help_label.pack()

def show_instruction():
    help_text = """
    Added instruction here
    """

    help_window = tk.Toplevel(root)
    help_window.title("Help")

    help_label = tk.Label(help_window, text=help_text, padx=10, pady=10, justify='left')
    help_label.pack()

def show_fullcode():
    help_text = """
    Added full code here
    """  

    help_window = tk.Toplevel(root)
    help_window.title("Help")

    # Create a scrollable text area
    scroll_text = tk.Text(help_window, padx=10, pady=10, wrap="word")
    scroll_text.insert("1.0", help_text)
    scroll_text.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the text area
    scrollbar = tk.Scrollbar(help_window, command=scroll_text.yview)
    scrollbar.pack(side="right", fill="y")
    scroll_text.config(yscrollcommand=scrollbar.set)


menu_bar = Menu(root)
root.config(menu=menu_bar)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="Show Information", command=show_help)
help_menu.add_command(label="Show Instruction", command=show_instruction)
help_menu.add_command(label="Show Full Code", command=show_fullcode)

root.mainloop()

