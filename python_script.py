#1. IMPORT LIBRARIES
import subprocess
import webbrowser
import pyautogui


#2. OPEN APP TO RECORD TIME 
subprocess.call(["open", "-a", "PUNCH"])

# Note: App named "PUNCH" is not an actual app; just replace "PUNCH" with actual app you'd like to open


#3. ASK IF USER HAS RECORDED TIME, BEFORE STARTING A TIMER 
pyautogui.alert("Clocked in? Let me remind you when to clock out :)")

# Note: Alternatively, use pyautogui.confirm instead of pyautogui.alert, to give options [OK / CANCEL]
# 	Then, above code can be re-written as below:
# answer = pyautogui.confirm("PUNCHED IN? Let me remind you when to punch out :)")
# if answer == 'Cancel':
#     quit()


#4. CLOSE TIME-RECORD APP
subprocess.run(["killall", "PUNCH"])

# Note: alert box will not be closed until script is finished. (whole steps are done)
# It will stay running as a proof that RPA has not been completed.
# Tip: how to manually shut RPA? use below to force shut the execution:
# Command + Option + Esc


#5. OPEN NECESSARY WEBSITES
webbrowser.open("https://www.web1.com")
webbrowser.open("https://www.web2.com")
webbrowser.open("https://www.web3.com")
webbrowser.open("https://www.web4.com")
webbrowser.open("https://www.web5.com")


#6. REMIND USER: 5 MIN BEFORE CLOCK-OUT (EX. USER TAKING 1H LUNCH):
### Apple Script has been inserted

def reminder():
    cmd = """
    set time1 to (minutes of (current date)) + 535
    repeat
	delay 1
	if minutes of (current date) = time1 then
		
		set variableWithSoundName to "Sonar"
		tell application "Finder" to activate
		display notification "5 min left to clock out!" with title "CLOCK OUT" sound name variableWithSoundName
                return
	end if
    end repeat
    """
    result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    return result.stdout

print(reminder())


#7. REMIND USER: 1 MIN BEFORE CLOCK-OUT
### Apple Script has been inserted

def reminder2():
    cmd = """
    set time2 to (minutes of (current date)) + 4
    repeat
	delay 1
	if minutes of (current date) = time2 then
    	
		set variableWithSoundName to "Sonar"
		tell application "Finder" to activate
		display notification "1 min left to clock out!" with title "CLOCK OUT" sound name variableWithSoundName
                return
	end if
    end repeat
    """
    result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    return result.stdout

print(reminder2())


#END
