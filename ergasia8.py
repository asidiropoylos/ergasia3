#εργασία 8
#έκδοση python 3.6

print ("Γ---------------------------------------")
print ("|Εισαγωγή στην επιστήμη των υπολογιστών")
print ("|Εργασία 8")
print ("L---------------------------------------")

import tweepy

# LoadTwitterUserFollowers()
# Loads twitter followers for a given twitter user name
def LoadTwitterUserFollowers( cUserName ):
    nPageCounter = 0
    aUserFollowers = []
    for page in tweepy.Cursor(api.followers, id=cUserName).pages():
        nPageCounter += 1
        #print('Getting page {} for followers ids'.format(nPageCounter))
        for UserFollower in page:
            aUserFollowers.append(UserFollower.screen_name)
        if nPageCounter == 3: break
    return aUserFollowers

#(consumer key, consumer secret)
auth = tweepy.OAuthHandler("4Xd4whnc7wpom9UUUXqAUufzW", "fOrWFjVMN6D0SrNt3B4cOTQt9C5wS1uZ0A0FAZN0txrOO6eCBi")

#(access token, access token secret)
auth.set_access_token("2569091207-sPglEKz6Uxo4uHbQfTp7XX54rRMnIn9LFwF7jVN", "FYBeSt4qd0TuTG7hQVZ7zAh4L0m5wf4rVjb82wlC6g8FS")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

client = tweepy.API(auth)

# Ask user to type the two twitter user names
cUser1 = input(str('Πληκτρολογείστε όνομα του πρώτου χρήστη: @'))
cUser2 = input(str('Πληκτρολογείστε όνομα του δεύτερου χρήστη: @'))

names1 = LoadTwitterUserFollowers(cUser1)
#print ("--------------------")
#print ("Οι followers του 1ου:")
#print(names1)
names2 = LoadTwitterUserFollowers(cUser2)
#print ("--------------------")
#print ("Οι followers του 2ου:")
#print(names2)

names3 = list(set(names1).intersection(names2))

print ("--------------------")
if len(names3) == 0:
    print ("Δεν υπάρχουν κοινοί Followers")
else:
    print ("Οι κοινοί Followers είναι: ")
    for nCounter in range(len(names3)):
        print ("@", names3[nCounter])
