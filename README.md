# Motivation
- I don't want to do repetitive tasks.
- Every morning before I start working, I follow certain routine. (Ex) connect to VPN > clock-in (record time in) > open necessary websites > set alarm to clock-out (record time out)
- This is not only repetitive but also manual process. And, I make mistakes because sometimes I forget to set the alarm resulting in clocking out late. I want my codes to do these things for me.

## Part1: writing codes
- launch-to-start/pyscript.py: 
  - by opening the script, below will automatically start
  - (1) open app to clock in 
  - (2) ask user if they recorded time, and if YES is clicked, start timer 
  - (3) close time recording app '
  - (4) open necessary websites
  - (5) remind user (send notification) 5 min before clock-out
  - (6) remind user (send notification) 1 min before clock-out
- launch-to-start/applescript.applescript:
  - by opening the script, below will automatically start
  - (1) open app to clock in 
  - (2) input box pops up, user enters their phone number 
  - (3) confirmation box pops up, script continues if user confirms number
  - (4) open necessary websites
  - (5) send Message to user's phone number 1 min before clock-out + bring app to in front for clock-out
- button-to-start/pyscript.py:
  - by opening the script, user will have buttons to choose
  ![tkinter_gui](https://user-images.githubusercontent.com/91002274/223154126-9eb0f987-9456-41ba-8d1b-7839512d3247.png)
  - (1) button1: TBU
  - (2) button2: TBU
  - (3) button3: TBU
- button-to-start/pyscriptver2.py:
  - by opening the script, user will have buttons to choose
  ![ver2](https://user-images.githubusercontent.com/91002274/224464862-c5c9f84c-f549-4194-b23b-df1351f68ad6.png)


## Part2: converting scripts to executable app for distribution
- I want to share this wonderful tool to my friends so that we can save time together!
- python scripts: 
  - using PyInstaller, convert py script into app for distribution
  - ```terminal
    python -m PyInstaller --windowed script.py
    ``` 
- applescript:
  - go to File > Export > File Format: Application
  
## Part3: comparison - Python or AppleScript?
- pyscript(autostart).py: 
  - code-wise: (pros) Python is popular language hence there is lot of reference resources. (cons) if you have PATH issue, it may take lot of time and energy to debug and fix to get final app. See 3.zsh: command not found [DEBUGGING_NOTE](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md)
  - distribution-wise: in order to distribute app to the team, there is certain internal procedure I need to take as otherwise, teammate(end-user) will see the alert message *cannot be opened because it is from unidentified developer* . End-user can open the app anyway via [bypassing the security settings](https://support.apple.com/en-sg/guide/mac-help/mh40616/mac) but it is not recommended. Better to go through internal process of app verficiation. 
  - summary: app verification process is little bit complex, time consuming but it is good learning opportunity. Knowing how to securily distirbute python scripts will be helpful for the future usage.
- applescript(autostart).applescript:
  - code-wise: (pros) it feels like Mac-apps are responding faster than when using Python scripts (cons) less resources to refer to comparing to Python. Also, AppleScript is only working on MacOS
  - distribution-wise: TBU
  - summary: TBU
- pyscript(w_buttons).py:
  - TBU  

## Part4: debugging notes
- for debugging notes, check main [DEBUGGING_NOTE](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md) under Python-practice


~ update in progress ~
