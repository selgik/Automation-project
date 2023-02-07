#1. IMPORT LIBRARIES
import subprocess
import webbrowser
import pyautogui


#2. OPEN TIME APP
subprocess.call(["open", "-a", "TIME"])


#3. ASK IF USER HAS PUNCHED IN, BEFORE STARTING A TIMER 
pyautogui.alert("PUNCHED IN? Let me remind you when to punch out :)")

# Note: Alternative: instead of pyautogui.alert, use pyautogui.confirm to give options [OK / CANCEL]
# answer = pyautogui.confirm("PUNCHED IN? Let me remind you when to punch out :)")
# if answer == 'Cancel':
#     quit()


#4. CLOSE TIME APP
subprocess.run(["killall", "TIME"])

# Note: alert box will not be closed. It will stay running as a proof that RPA has not been completed.
# Tip: how to manually shut RPA? use below to force shut the execution:
# Command + Option + Esc


#5. OPEN NECESSARY WEBSITES
webbrowser.open("https://www.web1.com")
webbrowser.open("https://www.web2.com")
webbrowser.open("https://www.web3.com")
webbrowser.open("https://www.web4.com")
webbrowser.open("https://www.web5.com")


#6. REMIND USER: 5 MIN BEFORE PUNCHING OUT (EX. USER TAKING 45MIN LUNCH):
### Apple Script has been inserted

def reminder():
    cmd = """
    set time1 to (minutes of (current date)) + 520
    repeat
	delay 1
	if minutes of (current date) = time1 then
		
		set variableWithSoundName to "Sonar"
		tell application "Finder" to activate
		display notification "5 min left to punch out!" with title "PUNCH OUT" sound name variableWithSoundName
                return
	end if
    end repeat
    """
    result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    return result.stdout

print(reminder())


#7. REMIND USER: 1 MIN BEFORE PUNCHING OUT
### Apple Script has been inserted

def reminder2():
    cmd = """
    set time2 to (minutes of (current date)) + 4
    repeat
	delay 1
	if minutes of (current date) = time2 then
    	
		set variableWithSoundName to "Sonar"
		tell application "Finder" to activate
		display notification "1 min left to punch out!" with title "PUNCH OUT" sound name variableWithSoundName
                return
	end if
    end repeat
    """
    result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
    return result.stdout

print(reminder2())


#END
