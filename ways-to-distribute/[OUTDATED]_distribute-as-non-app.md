# UPDATE: MAY 27, 2023
### NOTE: BELOW INFORMATION IS WRONG. IN ORDER FOR USER TO RUN PYTHON SCRIPT, THEY WOULD ANYWAY HAVE TO INSTALL PYTHON IN THEIR MACHINE



# What if you cannot distribute your scripts as application?
### Few Reasons
- Application is great. End-user does not have to install anything but run the program!
- However, you may have difficulties distributing app converted from python script if you do not have developer ID or certificate to sign off. 
    - Why? You might have been able to distribute app and ask end-user to ignore security alert or go to Settings to allow distributed app from unknown developer, but it may not work in some security settings. 
- In such case, you have alternatives: 
    - distribute python scripts: but end-user must have python installed.
    - distribute script with virtual environment: hmm... it sounds complex.
    - or distirube as Services(MacOS): could be the easist way, not much to install or configure.

### Distirubte your script as 'Services'
- What is needed?
    - Folder, named 'Ops_Helper': later you are going to zip it up for distribution.
    - Inside the folder: (1) python script (2) 'Quick Action' file generated from Automator
- How are we going to trigger the workflow?
    - User puts 'Ops_Helper' to the Downloads folder and unzip it
    - Insdie the folder, user double clicks 'quick action' > system will auto-install it under 'Services'
    - User can go to Finder or Safari > Services tab > run installed 'Quick Action' which will trigger python script to run (GUI will pop up)

### How to create 'Quick Action' file from Automator?
1. Open Automator > File > New > Quick Action
2. Add Run AppleScript
```AppleScript
on run {input, parameters}
	
	set downloadPath to POSIX path of (path to downloads folder from user domain) --ref1
	set pythonScriptPath to quoted form of (downloadPath & "your_script.py") --ref2
	
	tell application "Terminal" --ref3
		do script "python3 " & pythonScriptPath
	end tell
	
	return input
end run
```
- ref1: Retrieve path to end-user's downloads folder 
- ref2: Create a complete path to user's download's folder > Ops_Helper > python script
- ref3: Open Terminal and run python script found in the path from ref2


### Tip: How to check, remove, amend Services?
- Go to Finder > Go > 'Library' (if you cannot find it, hold 'Option' key) > Services

