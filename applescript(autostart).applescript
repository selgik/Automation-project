-- PREREQUISITE: USER NEEDS TO HAVE Messages APP LOGGED IN ON THE MAC
-- FOR THE FIRST TIME USE, ACCESS-RELATED ALERT WILL POP UP. CLICK YES TO ALLOW RPA.


--1. OPEN APP TO RECORD TIME 
--Note: "PUNCH" is not an actual app; just replace "PUNCH" with actual app name you'd like to open
tell application "PUNCH"
	launch
	activate
end tell


--2. USER INPUTS THEIR PHONE NUMBER TO GET NOTIFICATION.
--Note: tell me to activate --> this will bring a specified application or script to the front
tell me to activate
display dialog "Enter your phone number, if you want to get notification for clock-out" default answer "+65-"
set answer to text returned of result
display dialog "Your phone number is: " & answer & ". I will remind you 1 min before clock out :)"


--3. OPEN FREQUENTLY USED WEBSITES
tell application "Safari"
	activate
	make new document
	set theURLs to {"https://web1.com", "https://web2.com", "https://web3.com", "https:web4.com", "http:web5.com"}
	repeat with theURL in theURLs
		tell window 1 to make new tab with properties {URL:theURL}
	end repeat
end tell


--4. SEND MESSAGE TO USER TO REMIND OF CLOCK-OUT AND BRING "PUNCH" APP IN FRONT
--Note: Msg will be sent after 8Hours 59minutes (1 min before clock-out, with 1H lunch)
--Note2: Below, two actions are happening simultaneously (send message + bring app in front) hence nested format is used.

-- [Outdated] set time1 to (minutes of (current date)) + 539
-- [Reason**] if user goes out for lunch and computer goes to sleep mode, timer will stop resulting in inaccurate calculation.

set time1 to (current date) + (539 * minutes)

repeat
	delay 1
	if minutes of (current date) = time1 then
		
		tell application "Messages"
			send "1MIN LEFT TO CLOCK OUT" to participant answer
			tell application "PUNCH"
				activate
			end tell
		end tell
		return
	end if
end repeat


-- END
