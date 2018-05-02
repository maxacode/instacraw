# instacraw
#Max Derevencha - 04/20/2018

What it does: 
From a list of users in a file it gets all of their post's URL's and LIKE's for those POSTs. 

Tested on: Python 3.5 - 3.6: Ubuntu, Windows 10.


InstaCrawl Info/Instructions:
1) Users file File must be in same directory - Named = users.txt - File will be created on first run.
2) Run manually OR
3) Schedule via CHRON/Scheduler
4) Sight back and drink some coffee. 
5) Takes about 2 seconds (Depending on quality of USERNAMES and how many posts) to get URL and LIKES for each user. 
            ex: 5 users * 10 pics each = 50total * 2sec = 100sec  or 1min 40sec. 



Features:
0) Completely HANDS OFF after USERS in file specified. 
1) Master database of all scraped URL's.
2) Gets all the likes for all the posts for that specific user.
3) Create file under Users folder with current date. -Adds on if run same day multiple times. 
4) No duplicates in master databse or user file.
5) Gets all user's post URL's for all users in file.
6) Logs most ERRORs to ErrorLOGS Folder to todays date file. 




TODO:

0) OPTIMIZE for SPEED LIKE CRAZY
0) MAKE DEF's
1) Get # of views for each video. 
2) Rotating Instagram Accounts for PRIVATE Profile USE.
3) Rotating Proxy Capabilities - with user specified times.
4) INI for more customization. 
5) Capture more USER INFO: Followers, Following, Date posted, POST Frequency, All Comments, Popular Likers, etc.
6) Upload/Send - FTP, SMTP, SMB.
7) Remove BLANK and WRONG usernames from the file. 
9) GUI mode 
10) Complete SILENT mode
11) Graph results over time Period.
12) PASS USERs File name that way different lists can be run different times. 
