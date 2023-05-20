# Motivation
- I don't want to do repetitive tasks.
- Every morning before I start working, I follow certain routine. (Ex) connect to VPN > clock-in (record time in) > open necessary websites > set alarm to clock-out (record time out)
- This is not only repetitive but also manual process. And, I make mistakes because sometimes I forget to set the alarm resulting in clocking out late. I want my codes to do these things for me.

## Part1: GUI
### Launch-To-Start type: 
User simply launches script and automation will be triggered
- launch-to-start/pyscript.py: no GUI
  - (1) open app to clock in: user records their shift start time 
  - (2) input box pops up: user enters their phone number to get notification
  - (3) confirmation box pops up: script continues if user confirms phone number
  - (4) open necessary websites: pre-set websites will be opened in one window
  - (5) send MSG to set phone number: message will be sent 1 min before clock-out.  
  - (6) open app to clock out: user records their shift ending time 

- launch-to-start/applescript.applescript: no GUI
  - (1) open app to clock in: user records their shift start time
  - (2) notification pops up: ask user if they recorded time. If YES, start timer
  - (3) close time recording app 
  - (4) open necessary websites: pre-set websites will be opened in one window
  - (5) send notification: remind user 5 min before clock-out
  - (6) send notification: remind user 1 min before clock-out

### Button-To-Start type: 
User can click button to trigger automation  
- button-to-start/pyscript.py: 
- ![v1](https://user-images.githubusercontent.com/91002274/224491748-53b197d1-c49e-44d4-9598-708dbca0e6d7.png)
  - Clock Reminder: by clicking this button, timer (preset ex. 9h) will start
  - Lunch Reminder: by clicking this button, timer (preset ex. 1h) will start
  - Web Opener: by clicking this button, pre-set websites will be opened in one window

- button-to-start/pyscriptver2.py:
- ![v2](https://user-images.githubusercontent.com/91002274/224491751-272c651b-da41-4e96-bd9f-53f02e3a8f81.png)
  - Your Clock Time: user types in their shift start time (in HH:MM format)
  - Your Lunch Time: user types in the minutes they took for lunch (in MM format)
  - Set Alarm: by clicking this button, user will get alert when to clock-out
  - Open URL: by clicking this button, pre-set websites will be opened in one window
  - Instructions: by clicking this button, user will see another window containing texts with Next button 

- button-to-start/pyscriptver3.py:
- <img width="188" alt="t3" src="https://github.com/selgik/RPA-project/assets/91002274/2f261f9b-85d0-44ce-8d7d-42697cf95ca8">   

  - Your Clock Time: user types in their shift start time (in HH:MM format)
  - Your Lunch Time: user types in the minutes they took for lunch (in MM format)
  - Calculate Lunch: sub-window will pop up, user types in lunch start and end time in HH:MM format and hit enter
  - Set Alarm: by clicking this button, user will get alerted when to clock-out
  - Open URL: by clicking this button, saved websites will be opened in one window tab
  - Edit URL: by clicking this button, user can add/remove/edit URLs 
  - Troubleshoot: by clicking this button, user will see another window containing texts with Next button 

- button-to-start/pyscriptver4.py:
- <img width="188" alt="v4" src="https://github.com/selgik/Python-project/assets/91002274/c624694e-4a4a-4e3b-981d-84361a73a924"><img width="240" alt="st2" src="https://github.com/selgik/Python-project/assets/91002274/003eaef6-2124-408c-a64b-c0ceca7500a9">

  - Your Clock Time: user types in their shift start time (in HH:MM format)
  - Your Lunch Time: user types in the minutes they took for lunch (in MM format)
  - Calculate Lunch: sub-window will pop up, user types in lunch start and end time in HH:MM format and hit enter
  - Set Alarm: by clicking this button, user will get alerted when to clock-out
  - Stopwatch has been added: sub-window will pop up where user can record times and sum them all up.
  - Open URL: by clicking this button, saved websites will be opened in one window tab
  - Edit URL: by clicking this button, user can add/remove/edit URLs 


## Part2: Converting Scripts Into Executable App For Distribution
I want to share this wonderful tool to my friends so that we can save time together!
- python scripts: 
  - [NEW] using py2app, convert py script into app for distribution: check py_to_app folder
  - With PyInstaller, convert py script into app for distribution. Type in the Terminal: python3 -m PyInstaller --windowed script.py
 
- applescript:
  - Go to File > Export > File Format: Application
  
## Part3: Comparison - Python or AppleScript?
- Python:
  - code-wise: (pros) Python is popular language and there is lot of reference resources. You can also use various packages and be creative in developing GUI too (cons) if you have PATH issue, it may take lot of time and energy to debug and fix to get final app. See 3.zsh: command not found [DEBUGGING_NOTE](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md)
  - distribution-wise: in order to distribute app to the team at workplace, there could be certain internal procedure I may have to clear as otherwise, teammate(end-user) will see the alert message *cannot be opened because it is from unidentified developer* . End-user can open the app anyway via [bypassing the security settings](https://support.apple.com/en-sg/guide/mac-help/mh40616/mac) but it is not recommended. Better to go through internal process of app verficiation. 
  - summary: app verification process is little bit complex, time consuming but it is good learning opportunity. Comparing to Applescript, I can be much more flexible and creative with Python.
- Applescript:
  - code-wise: (pros) it feels like MacOS built-in apps are responding faster than when using Python scripts (cons) less resources to refer to comparing to Python. Also, AppleScript is only working on MacOS
  - distribution-wise: Conversion process into app is more straightforward. However, like python app I need to take certain internal procedure to distribute app internally to the team at workplace. 
  - summary: app verification is simpler, responses seem to be faster especially for MacOS built-in Apps. However there is less room to be creative due to Applescript being inflexible comparing to Python having lots of packages options.

## Part4: Debugging Notes
- for debugging notes, check main [DEBUGGING_NOTE](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md) under Python-practice


~ update in progress ~
