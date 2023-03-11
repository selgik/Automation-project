# Motivation
- I don't want to do repetitive tasks.
- Every morning before I start working, I follow certain routine. (Ex) connect to VPN > clock-in (record time in) > open necessary websites > set alarm to clock-out (record time out)
- This is not only repetitive but also manual process. And, I make mistakes because sometimes I forget to set the alarm resulting in clocking out late. I want my codes to do these things for me.

## Part1: GUI
- launch-to-start/pyscript.py: 
  - There is no GUI. By opening the script, sequence of events will automatically start
- launch-to-start/applescript.applescript:
  - There is no GUI. By opening the script, sequence of events will automatically start
- button-to-start/pyscript.py:
  - by opening the script, user will have buttons to choose
  ![tkinter_gui](https://user-images.githubusercontent.com/91002274/223154126-9eb0f987-9456-41ba-8d1b-7839512d3247.png)
  - (1) button1: Clock Reminder
  - (2) button2: Lunch Reminder
  - (3) button3: Web Opener
- button-to-start/pyscriptver2.py:
  - by opening the script, user will have form to fill in and buttons to choose
  ![v2](https://user-images.githubusercontent.com/91002274/224464991-49183392-3b60-440e-99b3-230a32ac24be.png)
  - (1) form1: Clock Time (in HH:MM format)
  - (2) form2: Lunch Time (in MM format)
  - (3) button1: Set Alarm
  - (4) button2: Open URL
  - (5) button3: Instructions

## Part2: Action Flow
- launch-to-start/pyscript.py: 
  - by opening the script, below events will automatically start
  - (1) open app to clock in: user records their shift start time
  - (2) notification pops up: ask user if they recorded time. If YES, start timer
  - (3) close time recording app 
  - (4) open necessary websites: pre-set websites will be opened in one window
  - (5) send notification: remind user 5 min before clock-out
  - (6) send notification: remind user 1 min before clock-out
- launch-to-start/applescript.applescript:
  - by opening the script, below will automatically start
  - (1) open app to clock in: user records their shift start time 
  - (2) input box pops up: user enters their phone number to get notification
        *number can be saved in the script to prevent from typing in in the future*
  - (3) confirmation box pops up: script continues if user confirms phone number
  - (4) open necessary websites: pre-set websites will be opened in one window
  - (5) send MSG to set phone number: message will be sent 1 min before clock-out.  
        app to record clock-out will be automatically pop up in front too.
- button-to-start/pyscript.py:
  - by opening the script, user will have buttons to choose
  - (1) button1: TBU
  - (2) button2: TBU
  - (3) button3: TBU
- button-to-start/pyscriptver2.py:
  - by opening the script, user will have buttons to choose
  - (1) form1: TBU
  - (2) form2: TBU
  - (3) button1: TBU
  - (4) button2: TBU
  - (5) button3: TBU

## Part3: Converting Scripts Into Executable App For Distribution
- I want to share this wonderful tool to my friends so that we can save time together!
- python scripts: 
  - using PyInstaller, convert py script into app for distribution
  - ```terminal
    python -m PyInstaller --windowed script.py
    ``` 
- applescript:
  - go to File > Export > File Format: Application
  
## Part4: Comparison - Python or AppleScript?
- Python:
  - code-wise: (pros) Python is popular language hence there is lot of reference resources. You can also use various packages and be creative in developing GUI too (cons) if you have PATH issue, it may take lot of time and energy to debug and fix to get final app. See 3.zsh: command not found [DEBUGGING_NOTE](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md)
  - distribution-wise: in order to distribute app to the team at workplace, there is certain internal procedure I need to take as otherwise, teammate(end-user) will see the alert message *cannot be opened because it is from unidentified developer* . End-user can open the app anyway via [bypassing the security settings](https://support.apple.com/en-sg/guide/mac-help/mh40616/mac) but it is not recommended. Better to go through internal process of app verficiation. 
  - summary: app verification process is little bit complex, time consuming but it is good learning opportunity. Comparing to Applescript, I can be much more flexible and creative with Python.
- Applescript:
  - code-wise: (pros) it feels like MacOS built-in apps are responding faster than when using Python scripts (cons) less resources to refer to comparing to Python. Also, AppleScript is only working on MacOS
  - distribution-wise: Conversion process into app is more straightforward. However, like python app I need to take certain internal procedure to distribute app internally to the team at workplace. 
  - summary: app verification is simpler, responses seem to be faster especially for MacOS built-in Apps. However there is less room to be creative due to Applescript being inflexible comparing to Python having lots of packages options.

## Part5: debugging notes
- for debugging notes, check main [DEBUGGING_NOTE](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md) under Python-practice


~ update in progress ~
