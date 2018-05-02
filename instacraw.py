# Max Derevencha - 417Code
# 4/24/2018 -
# From a list of users in a file it gets RECENT 12 PIC URL's and (LIKE's) for those PICs.
# InstaCrawl Info/Instructions:

# Tested on: Python 3.5-6: Ubuntu, Windows 10.

# What it does:
# From a list of users in a file it gets RECENT 12 PIC URL's and (LIKE's) for those PICs.


# 1) Users file File must be in same directory - Named = users.txt - Will autocreate on first run.
# 2) Run manually
# 3) Schedule via CHRON/Scheduler
# 4) Sight back and drink some coffee.

# Additional installations:
# apt install python-pip
# pip install -U selenium

# Importin RE for searchign and URLLIP.rfequest to READ URL's
import re
import urllib.request
import time
import datetime
import os
from selenium import webdriver

####CODE STARTEED####

# var to have loop go through usernames
numofuser = 0
# All links go here
alllinks = []
# assigning basic variables
instaurl = ("https://www.instagram.com/")
# Error out variable
curError = []
# Bad link errors go here
notGoodLink = []
# searching for this to take PIC ID before it.
search2 = "edge_media_to_comment"
# Searching for taken-by
search = "taken-by"
# Var for what keyword to search for the LIKES info
likeSearch = "Likes"
# var to delay when program scrolls down to new page.
delayLoad = 2
#pic id
picid = ""
#final
final = ""
#All insta ID's
instaIDAll = []

# looks if users.txt exists if not then creates it.
usrFile = "users.txt"
if os.path.isfile(usrFile):
    with open(usrFile, 'r')as f:
        usernames = [line.strip() for line in f]
        print("These are all the usernames: " + str(usernames))
else:
    usernames = open(usrFile, "w+")
    print("users.txt was created, go and enter all user names, then lauch program again.")
    input()

# gets the total number of users in the users file.
numusers = sum(1 for line in open('users.txt'))
print(str(numusers) + " total usernames in file")

# Starting the process
print("Starting the Scraping Process")

driver = webdriver.Firefox(executable_path="geckodriver/geckodriver")

# Loop that runs for every USER in teh file
for run in range(numusers):
    try:
        print("Starting process for user: " + usernames[numofuser])
        # total pic
        totalPic = 1

        # Var to show how many PICS Per User
        int = 0
        # Array for final result
        finalUserAll = []
        # print(usernames[numofuser])
        # Making full URL with username
        fullurl = instaurl + usernames[numofuser]

        #driver = webdriver.Firefox(executable_path="geckodriver/geckodriver")
        driver.get(fullurl)



        counter = 0
        while counter < 60:
            ##print("Scrolling Again")
            ##print("----------------------------------------------------------------------")

            #scrolling this page 3 
            for x in range(0, 3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(delayLoad)
                newHeight = driver.execute_script("return document.body.scrollHeight")


            # putting page source into var
            data1 = driver.page_source

            # Parsing and adding all to list
            data2 = re.sub(r"[^\w-]", " ", data1).split()
            # print(data2)
            # Getting the count for number of posts for REFERENCE in later loop.
            ##searchcount = data2.count(search2) + data2.count(search)
            ##print("Search Count: " + str(searchcount))

            #Var for this data source since new page source is gotten every time it scrolls.
            instaID = 0
            ##print("Insta ID: " + str(instaID))

            # Starting loop to find all the URL's on the site.
            for i, j in enumerate(data2):
                if j == search2 or j == search:

                    ##print("I: " + str(i))
                    ##print("instaID: " + str(instaID))
                    ##print("Total PIC: " + str(totalPic))

                    # Int to have numbers in the results
                    int = int + 1

                    # Found the INDEX right before the URL value so adding one to get final URL INDEX
                    instaID = i - 1

                    #Checking if current picID already in list of picID's for this user. IF not then doing whole process.
                    if data2[instaID] not in instaIDAll:

                        # Making full URL for all the PIC's
                        picid = "https://instagram.com/p/" + data2[instaID]

                        ##print("pic id: " + str(picid))

                        # Getting website source into variables
                        datalike = urllib.request.urlopen(picid).read()
                        # decding to UTF-8
                        datalike1 = datalike.decode("utf-8")
                        # Finding keyword stored in LIKESEARCH for the likes INDEX
                        datalike2 = re.search(likeSearch, datalike1)

                        ##print("datalike2 Done")

                        # Cropping out all the CHARS around the like count.
                        start = datalike2.start() - 10
                        end = datalike2.start()
                        finalLike = datalike1[start:end]

                        ##print("Final Like Done")

                        # Cropping out even more to get exact like ammount
                        datalike2 = re.search('="', finalLike)
                        start = datalike2.end()
                        finalLike3 = finalLike[start:]

                        ##print("final like 3 done")

                        # Making FINAL STRING
                        final = (str(totalPic) + " | " + str(datetime.datetime.now()) + " | " + usernames[
                            numofuser] + " | " + finalLike3 + " | " + picid)

                        #Increasing counter for number of posts.
                        totalPic = totalPic + 1

                        ##print("Final Done")

                        # Appending all links to master file
                        alllinks.append(picid)

                        # Appeding FINAL to CURRENT USER
                        finalUserAll.append(final)

                        #Appending instaID to the list so we can compare once it runs again.
                        instaIDAll.append(data2[instaID])

                        #Reseting the counter cuz we have found some more that are not in list.
                        counter = 0

                    else:
                        #If instaID already in list then add to counter and continue
                        ##print("Already done this one")
                        i = i + 10
                        instaID = instaID + 10

                        #If to many already in list then its scrolled to the bottom probably.
                        counter = counter + 1
                        ##print("Counter: " + str(counter))

                    #### END OF IF instaID in ALL array.
                ### END OF IF J IN SEARCH or SEARCH2
            ### END OF Enumerating i for J in data2
        ### END OF WHILE


        # Reseting for current user.
        int = 0

        # writing to master file and making sure the URL is not already in there.
        outAllLinks = open("AllLinks.txt", "a")
        for line in alllinks:
            if alllinks[int] in open("AllLinks.txt").read():
                int = int + 1
            else:
                outAllLinks.write(line)
                outAllLinks.write("\n")
        outAllLinks.close()

        # writing to users file.
        currentDate = datetime.datetime.now().strftime("%m-%d-%y")
        filename = "AllData/" + usernames[numofuser] + "/" + currentDate + ".txt"
        directory = "AllData/" + usernames[numofuser]
        if not os.path.exists(directory):
            os.makedirs(directory)
        outfinalUserAll = open(filename, "a")
        for line in finalUserAll:
            outfinalUserAll.write(line)
            outfinalUserAll.write("\n")
        outfinalUserAll.close()

        # Stopping browser driver for this user.
        #driver.quit()

        # Keep Going with all the USERNAMES
        numofuser = numofuser + 1

    ### TRY AND EXCEPT HERE

    except Exception as error:
        currentDate = datetime.datetime.now().strftime("%m-%d-%y")
        print(error)
        curError = (str(datetime.datetime.now()) + " | " + usernames[numofuser] + " | " + str(error))

        # Writing error to todays error log
        directory2 = "ErrorLOGS/"
        if not os.path.exists(directory2):
            os.makedirs(directory2)
        errorOut = open(directory2 + currentDate + " ErrorLog.txt", "a")
        errorOut.write(curError)
        errorOut.write("\n")
        errorOut.close()
	
        continue

driver.quit()
print("All Done, Thanks!")
#input()
