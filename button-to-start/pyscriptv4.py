#1. Libraries
from tkinter import messagebox
import datetime
import os
import subprocess
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
        result_label.config(text=f"Clock Out at {hour:02d}:{minute:02d}")
    except ValueError:
        messagebox.showinfo("Alert", "[ERROR] Enter Time Correctly!")

## Function for "Set Alarm" button(purpose: validate entries)
def set_alarm():
    global alarm_thread

    if result_label["text"] == "":
        punch_calculator()
    else:
        if alarm_thread and alarm_thread.is_alive():
            global running
            running = False
            alarm_thread.join()
            punch_calculator()

    set_time = result_label["text"][13:]
    messagebox.showinfo("Confirmation", "Alarm set!")
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
            return result.stdout
            break
        time.sleep(1)
    
## Function for "Open URL" button
def openURL():
    # Create a file to store URLs if it doesn't exist
    if not os.path.exists("ops_helper_urls.txt"):
        with open("ops_helper_urls.txt", "w") as f:
            f.write("https://apple.com\n")

    # Read the URLs from the file
    with open("ops_helper_urls.txt", "r") as f:
        urls = f.read().splitlines()
    for url in urls:
        webbrowser.open_new_tab(url)

## Function for "Edit URL" button
def editURL():
    sub_window("Edit URL")
    lab_url1 = tk.Label(sub_window_global, text="Your URL(s)")
    lab_url1.pack()
    
    # Read the URLs from the file and populate the input fields with them
    if not os.path.exists("ops_helper_urls.txt"):
        with open("ops_helper_urls.txt", "w") as f:
            f.write("https://apple.com\n")

    with open("ops_helper_urls.txt", "r") as f:
        urls = f.read().splitlines()

    num_entries = len(urls)
    entries = []

    for i in range(num_entries):
        entry = tk.Entry(sub_window_global)
        entry.insert(0, urls[i])
        entry.pack()
        entries.append(entry)

    # Create a new entry field above the "Add" and "Save" buttons
    def create_new_field():
        new_entry = tk.Entry(sub_window_global)
        new_entry.pack()
        entries.append(new_entry)
        # Repack the "Add" and "Save" buttons to keep them at the bottom
        add_button.pack(side=tk.BOTTOM)
        save_button.pack(side=tk.BOTTOM)

    # Save the URLs entered by the user to the file
    def save_urls():
        urls = [entry.get() for entry in entries]
        with open("ops_helper_urls.txt", "w") as f:
            for url in urls:
                f.write(url + "\n")
        sub_window_global.destroy()

    add_button = tk.Button(sub_window_global, text="Add", command=create_new_field)
    add_button.pack(side=tk.BOTTOM)
    
    save_button = tk.Button(sub_window_global, text="Save", command=save_urls)
    save_button.pack(side=tk.BOTTOM)

## Function to alert before closing stopwatch
def close_window():
    result = messagebox.askquestion("Confirmation", "Are you sure you want to close?")
    if result == "yes":
        sub_window_global.destroy()
    
## Function for "Stopwatch" button
def stopwatch():
    sub_window("Stopwatch")

    sst1 = ""
    sst2 = ""
    label_row = 2  # Initial row index for label_records

    def stamp_start_time():
        nonlocal sst1
        stamp_start_time = datetime.datetime.now()
        sst1 = stamp_start_time.strftime("%H:%M:%S")
        label_start.config(text=sst1)

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
            
        except Exception as e:
            pass

    def sumup():
        initial_min_stopwatch = sum(sum_min_list)
        additional_min_stopwatch = sum(sum_sec_list) // 60
        total_min_stopwatch = initial_min_stopwatch + additional_min_stopwatch
        total_sec_stopwatch = sum(sum_sec_list) % 60

        label_total_time = tk.Label(sub_window_global, \
                                    text=f"Total {total_min_stopwatch} minutes {total_sec_stopwatch} seconds",\
                                    fg="#009900")
        label_total_time.grid(row=label_row, column=0, columnspan=4)
                    
    def reset_start_button():
        label_start.config(text="")

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
    
    sub_window_global.protocol("WM_DELETE_WINDOW", close_window)
    sub_window_global.mainloop()

    
#3. Main Window 
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Ops Helper")


#4. Labels, Entries and Images
label1 = tk.Label(root, text="Your Punch Time (HH:MM)")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Your Lunch Time (MM)")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()    
    
entry2.bind("<Return>", lambda event: punch_calculator())

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

version_label = tk.Label(root, text="Sylvia-GUI-prj-May2023", fg="gray")
version_label.pack()

root.mainloop()
