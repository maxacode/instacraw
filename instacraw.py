#Max Derevencha - 417Code
#4/24/2018 -
#From a list of users in a file it gets RECENT 12 PIC URL's and (LIKE's) for those PICs.
#InstaCrawl Info/Instructions:

#Tested on: Python 3.6: Ubuntu, Windows 10.

#What it does: 
#From a list of users in a file it gets RECENT 12 PIC URL's and (LIKE's) for those PICs. 


#1) Users file File must be in same directory - Named = users.txt - Do not have extra line at the end. 
#2) Run manually 
#3) Schedule via CHRON/Scheduler
#4) Sight back and drink some coffee. 


#Features:
#Master database of all scraped URL's.
#Creates separate folders for all users. 
#Create file under Users folder with current date. -Adds on if run same day multiple times. 
#Specifies users for user folder. 
#Gets Recent 12 PIC URL's of all USERS


#TODO:
#Get number of likes for each picture. 
#Rotating Instagram Accounts.
#Rotating Proxy Capabilities - with user specified times.
#INI for more config features. 
#Capture more USER INFO: Followers, Following, Date posted, POST Frequency, All Comments, Popular Likers, etc.
#Send/Upload via - FTP, SMTP, SMB.



#Importin RE for searchign and URLLIP.rfequest to READ URL's
import re
import urllib.request
import time
import datetime
import os


#from selenium import webdriver
from bs4 import BeautifulSoup

#var to have loop go through usernames
numofuser = 0

#All links go here
alllinks = []

#CODE BEGINS



#TRY For Error Catching

#try:

    #assigning basic variables
instaurl = ("https://www.instagram.com/")

    #Catching if file exists
#try:
        #usernames from file
usrFile = "users.txt"
if os.path.isfile(usrFile):
    with open(usrFile,'r')as f:
        usernames = [line.strip() for line in f]
        print(usernames)
else:
    usernames = open(usrFile,"w+")

    #try:
numusers = sum(1 for line in open('users.txt'))
print(numusers)
    #except:
#print("Some error in users file")         
    #except:
#createusernamesfile = open("users.txt","w+")
#print("File was not found, we created it for you so not just put all usernames in there")

    #Adding all usernames to list
    #try:

    #except:
   #     print("Was not able to append all usernames")




    #Try for looping the url together
    #try:
print('-------------------------------')
for run in range(numusers):
    print('-------------------------------')
    #Var to show how many PICS Per User
    int = 0
    #Array for final resul
    finalUserAll = []
    #Making full URL with username
    fullurl = instaurl + usernames[numofuser]
    #Backup search string search = ',"shortcode":"'
    search2 = "shortcode"

    #website data var
    data = urllib.request.urlopen(fullurl).read()
    #decoding to UTF-8
    data1 = data.decode("utf-8")
    #Parsing and adding all to list
    data2 = re.sub(r"[^\w]", " ", data1).split()

    #Getting the count for number of posts for REFERENCE
    searchcount = data1.count(search2)
    #print(searchcount)

    #Starting loop to find all the URL's on the site.
    if search2 in data2:
        #print("test1")
        for i, j in enumerate(data2):
            #print('test2')
            if j == search2:
                int = int + 1
                #print("test3")
                instaID = i +1
                #print(instaID)
                tempurl = data2[instaID]
                #print(tempurl)
                #Making sure the lenght of the URL is properly 11 CHARS
                if len(tempurl) == 11:
                    picid = "https://instagram.com/p/" + data2[instaID]
                    #print("test4")
                    #print("IF STATEMENT")
                    #Making FINAL STRING
                    final = (str(int) + " | " + str(datetime.datetime.now()) + " | " +  usernames[numofuser] + " | " + picid)

                    #Appending all links to master file
                    alllinks.append(picid)
                    #Appeding FINAL to CURRENT USER
                    finalUserAll.append(final)






                #If Not then adding second string
                elif len(tempurl) < 11:
                    instaID2 = i + 2
                    picid = "https://instagram.com/p/" + data2[instaID] + "-" + data2[instaID2]
                    #print("test5----------------------------------------")
                    #Making FINAL STRING
                    final = (str(int) + " | " + str(datetime.datetime.now()) + " | " +  usernames[numofuser] + " | " + picid)

                    #Appending all links to master file
                    alllinks.append(picid)
                    #Appeding FINAL to CURRENT USER
                    finalUserAll.append(final)




                #Tossing LINK away if not correct
                else:
                    print("Sorry not a valid link, tossing it away")
                    continue



    int = 0
    #writing to master file and making sure the URL is not already in there.
    outAllLinks = open("AllLinks.txt","a")
    for line in alllinks:
        if alllinks[int] in open("AllLinks.txt").read():
            int = int + 1
        else:
            outAllLinks.write(line)
            outAllLinks.write("\n")
    outAllLinks.close()


    #writing to users file.
    currentDate = datetime.datetime.now().strftime("%m-%d-%y")
    filename = usernames[numofuser]+"/"+currentDate+ ".txt"
    if not os.path.exists(usernames[numofuser]):
        os.makedirs(usernames[numofuser])
    outfinalUserAll = open(filename,"a")
    for line in finalUserAll:
        outfinalUserAll.write(line)
        outfinalUserAll.write("\n")
    outfinalUserAll.close()

 #Keep Going with all the USERNAMES
    numofuser = numofuser + 1



    #for i in range(searchcount):
    #looping through all teh shortcodes.

        #Searching for meta lcoaiton of the pic id:
        #rawpicid = re.search(',"shortcode":"',data1)

        #starting of new search param
      #  start = rawpicid.start()
       # end = start + 25
#
        #String with new search params
      #  picid = data1[start:end]

       # picid1 = picid[14:25]
      #  picurl = instaurl + 'p/' + picid1
        #print(usernames[numofuser])
       # print(picurl)
       # print(searchcount)
        #searchcount = searchcount + 1

print("All Done, Press enter to Exit")
input()
