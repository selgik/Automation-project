# Motivation
- I don't want to do repetitive tasks.
- Every morning before I start working, I follow certain routine. (Ex) connect to VPN > clock-in (record time in) > open necessary websites > set alarm to clock-out (record time out)
- This is not only repetitive but also manual process. And, I make mistakes because sometimes I forget to set the alarm resulting in clocking out late. I want my codes to do these things for me.

## Part1: writing codes
- python_script.py: 
  - (1) open app to clock in 
  - (2) ask user if they recorded time, and if YES is clicked, start timer 
  - (3) close time recording app '
  - (4) open necessary websites
  - (5) remind user (send notification) 5 min before clock-out
  - (6) remind user (send notification) 1 min before clock-out
- apple_script.applescript:
  - (1) open app to clock in 
  - (2) input box pops up, user enters their phone number 
  - (3) confirmation box pops up, script continues if user confirms number
  - (4) open necessary websites
  - (5) send Message to user's phone number 1 min before clock-out + bring app to in front for clock-out
  
## Part2: converting scripts to executable app for distribution
- I want to share this wonderful tool to my friends so that we can save time together!
- python_script.py: 
  - using PyInstaller, convert py script into app for distribution
  - ```terminal
    pyinstaller --windowed python_script.py
    ``` 
- apple_script.applescript:
  - go to File > Export > File Format: Application
  
## Part3: comparision - Python or AppleScript?
- python_script.py: 
  - code-wise: (pros) Python is popular language hence there is lot of reference resources. (cons) if you have PATH issue, it may take lot of time and energy to debug and fix to get final app. See 3.zsh: command not found [debugging note](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md)
  - distribution-wise: in order to distribute app to the team, there is certain procedure I need to take as otherwise, teammate(end-user) will see the alert message *cannot be opened because it is from unidentified developer* . End-user can open the app anyway via [bypassing the security settings](https://support.apple.com/en-sg/guide/mac-help/mh40616/mac) but it is not recommended. Better to go through internal process of app verficiation. 
  - summary: app verification process is little bit complex, time consuming but it is good learning opportunity. Knowing how to securily distirbute python scripts will be helpful for the future usage.
- apple_script.applescript:
  - code-wise: (pros) it feels like Mac-apps are responding faster than when using Python scripts (cons) less resources to refer to comparing to Python. Also, AppleScript is only working on MacOS
  - distribution-wise: TBU
  - summary: TBU

## Part4: debugging notes
- for debugging notes, check [main notes](https://github.com/selgik/Python-practice/blob/main/DEBUGGING_NOTE.md) under Python-practice


~ update in progress ~
