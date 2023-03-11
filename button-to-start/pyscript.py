#1. IMPORT LIBRARIES
import tkinter as tk
import threading
import subprocess
from tkinter import messagebox


#2. SETTING UP VARIABLES
# Below variables will be used in functions
# Note: "PUNCH" is not an actual app; just replace "PUNCH" with actual app name you'd like to open

script1 = """
tell application "PUNCH"
    launch
    activate
end tell

tell me to activate
display dialog "[REMINDER] MSG will be sent 1 min before clock out"
set answer to "+1-2345-6789"

set time1 to (current date) + (539 * minutes)

repeat
    delay 1
    if (current date) ≥ time1 then
        tell application "System Events"
            tell application process "Messages"
                set frontmost to true
            end tell
        end tell

        tell application "Messages"
            send "1MIN LEFT TO CLOCK OUT" to participant answer
        end tell
        return
    end if
end repeat
"""

script2 = """
tell application "PUNCH"
    launch
    activate
end tell

tell me to activate
display dialog "[LUNCH REMINDER] MSG will be sent 1 min before clock in"
set answer to "+1-2345-6789"

set time2 to (current date) + (59 * minutes)

repeat
    delay 1
    if (current date) ≥ time2 then
        tell application "System Events"
            tell application process "Messages"
                set frontmost to true
            end tell
        end tell

        tell application "Messages"
            send "1MIN LEFT TO CLOCK IN" to participant answer
        end tell
        return
    end if
end repeat
"""

script3 = """
tell application "Safari"
    activate
    make new document
    set theURLs to {"https://www.web1.com", "https://www.web2.com", "https://www.web3.com", "https://www.web4.com", "https://www.web5.comm"}
    repeat with theURL in theURLs
        tell window 1 to make new tab with properties {URL:theURL}
    end repeat
end tell
"""


#3. SETTING UP FUNCTIONS
# without threading module: user will not be able to run multiple scripts simultaneously as mouse will show 'running' icon.
# with threading module: user can run script1 and while waiting script 1 to end, can run other scripts 2 or 3.

subprocs = []

def click_btnp1():
    global subprocs
    proc1 = subprocess.Popen(['osascript', '-e', script1])
    subprocs.append(proc1)
    proc1.wait()

def click_btn1():
    threading.Thread(target=click_btnp1, daemon=True).start()

def click_btnp2():
    global subprocs
    proc2 = subprocess.Popen(['osascript', '-e', script2])
    subprocs.append(proc2)
    proc2.wait()

def click_btn2():
    threading.Thread(target=click_btnp2, daemon=True).start()

def click_btn3():
    subprocess.run(['osascript', '-e', script3])

def on_closing():
    global subprocs
    if tk.messagebox.askokcancel("Quit", "Are you sure you want to quit while the script is running?"):
        for proc in subprocs:
            if proc.poll() is None:
                proc.kill()
        root.destroy()

        
#4. CREATE WINDOW (GUI)
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Reminders")
root.resizable(False, False)

canvas = tk.Canvas(root, width=300, height=200, bg="black")
canvas.pack()


#5. LINK BUTTON WITH FUNCTIONS, PLACE THEM IN GUI
button1 = tk.Button(root, width=15, height=2, text="CLOCK REMINDER", font=("white", 10, "bold"),
                bg="yellow", command=click_btn1)
button1.place(x=90, y=50)

button2 = tk.Button(root, width=15, height=2, text="LUNCH REMINDER", font=("white", 10, "bold"),
                bg="yellow", command=click_btn22)
button2.place(x=90, y=90)

button3 = tk.Button(root, width=15, height=2, text="WEB OPENER", font=("white", 10, "bold"),
                bg="yellow", command=click_btn3)
button3.place(x=90, y=130)

root.mainloop()


# END
