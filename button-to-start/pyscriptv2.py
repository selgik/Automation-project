#1. LIBRARIES
import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser
import subprocess
import datetime
import time


#2. FUNCTIONS
#1) innitialize global variable to None which will be used in def check_time()
alarm_thread = None   

#2) def submit(): when user inputs clock-in time and lunch time, function will calculate time to clock-out
#handling error: if user inputs string values to clock time and lunch time > ValueError appears > alert MSG comes up
def submit():  
    try:
        time_str = entry1.get()
        hour, minute = map(int, time_str.split(":"))
        lunch_minute = int(entry2.get())
        total_minute = hour*60 + minute + 8*60 + lunch_minute
        hour = total_minute // 60
        minute = total_minute % 60
        result_label.config(text=f"Clock Out at {hour:02d}:{minute:02d}")
    except ValueError:
        messagebox.showinfo("Alert", "[ERROR] Enter Time Correctly!") 

#3) def check_time(): function will set alarm using previously calculated time from def submit()
#firstly, it will check whether user has input forms and calculated target time
#next, it will kill any ongoing alarm to override with new one. Otherwise it will start new alarm
#alarm_thread.start(): it will execute the check_current_time function in a separate thread of execution
def check_time():
    global alarm_thread

    if result_label["text"] == "":
        messagebox.showinfo("Alert", "[ERROR] Enter Time!")
    else:
        if alarm_thread and alarm_thread.is_alive():
            global running
            running = False
            alarm_thread.join()
            #This line waits for the alarm_thread to finish executing before moving on to the next line of code

        set_time = result_label["text"][13:]
        messagebox.showinfo("Confirmation", "Alarm set!")
        alarm_thread = threading.Thread(target=check_current_time, args=(set_time,))
        alarm_thread.start()

#4) def check_current_time(set_time): checks time until current time == target time (set time)
# below is the loop which checks current time with set time. When both time matches, it will show alert window
def check_current_time(set_time):
    global running  
    running = True
    while running:
        now = datetime.datetime.now()
        current_time = f"{now.hour:02d}:{now.minute:02d}"
        if current_time == set_time:
            messagebox.showinfo("Alert", "It's time to go home!")
            break
        time.sleep(1)

#4) def on_closing(): when user tries to close app, notification will pop up 
# if user clicks OK, it will stop the look in def check_current_time(set_time) and finish app
def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        global running
        running = False
        root.destroy()

#5) def openURL(): opens URLs as tabs in one Safari window
def openURL():
    urls=["https://url1.com","https://url2.com","https://url3.com","https:url4.com", "https://url5.com"]
    for url in urls:
        webbrowser.open_new_tab(url)
 
#6) show_instructions(): user can click 'next' button to see set of instruction texts
def show_instructions():
    instructions_list = [
        """STEP 1: aaa

        A1A1A1
        B1B1B1
        """,
        """STEP 2: bbb

        A1A1A1
        B1B1B1
        """,
        """STEP 3: ccc

        A1A1A1
        B1B1B1
        """,
        """STEP 4: ddd

        A1A1A1
        B1B1B1
        """,
        """STEP 5: eee

        A1A1A1
        B1B1B1
        """
    ]

    instruction_window = tk.Toplevel(root)
    instruction_window.geometry("300x140")
    instruction_window.title("Instructions")

    index = tk.IntVar(value=0)  # variable to keep track of the index
    instruction_label = tk.Label(instruction_window, text=instructions_list[index.get()])
    instruction_label.pack()

    def next_instruction():
        index.set((index.get() + 1) % len(instructions_list))  # update the index 
        instruction_label.config(text=instructions_list[index.get()])  # update the label text

    next_button = tk.Button(instruction_window, text="Next", command=next_instruction)
    next_button.pack()


#3. WINDOW 
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Ops_Assistant")


#4. LABELS AND ENTRIES
# texts entered in the Entry widget (entry1, entry2) will be retrieved and used in functions
label1 = tk.Label(root, text="Your Clock Time (HH:MM):")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Your Lunch Time (MM):")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

entry2.bind("<Return>", lambda event: submit())
#instead of creating SUBMIT button, I triggered ENTER keyboard with submit() 

result_label = tk.Label(root, text="", fg="yellow")
result_label.pack()


#5. BUTTONS
button1 = tk.Button(root, width=10, text="Set Alarm", command=check_time)
button1.pack()

button2 = tk.Button(root, width=10, text="Open URL", command=openURL)
button2.pack()

button3 = tk.Button(root, width=10, text="Instructions", command=show_instructions)
button3.pack()

version_label = tk.Label(root, text="SylviaK-RPA-Proj-Mar2023", fg="gray")
version_label.pack()

root.mainloop()


# END   
    
