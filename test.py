# To do:
# Get the titles of reddit submissions pulled from the pages
# Import the results of this script to a database
<<<<<<< HEAD
# Create another script to run this script on every reddit subreddit someone
# signed up on the website is subscribed to once an hour, and update results
# to the database.
   #Side-note, ensure validity of subreddit is checked before adding to master list


=======
# Create another script to run this script on every reddit subreddit someone is subscribed to every hour,
and update results to the database
   #Side-note, ensure validity of subreddit is checked before adding to master list

>>>>>>> 01616f8e313fa104dd5b05720630c741f8086594
from bs4 import BeautifulSoup
from urllib2 import Request
from urllib2 import urlopen
import codecs

#global variables
indexme = []
getusers = []
getvotes = []
getcomments = []
gethyperlinks = []
oldtitles = []

#Finds where a substring is located within a string
def find_indices(target, subst):
   returnme = []
   for i in range(len(target) - len(subst)):
      if target[i:i+len(subst)] == subst:
         returnme.append(i)
   if returnme == []:
      return '0'
   else:      
      return returnme
<<<<<<< HEAD
################################################
# Unused currently
=======

#####################################################
# Unused Currently. 
>>>>>>> 01616f8e313fa104dd5b05720630c741f8086594
def maketext(page):
   hdr = {'User-Agent' : 'RedditDigest Bot'}
   req = Request(page, headers = hdr)
   soupy = BeautifulSoup(page)
   soup = soupy.prettify()
   f = codecs.open('output.txt', 'w' 'utf-8')
   for i in range(len(soup)):
      try:
         soup[i].encode('utf-8')
      except:
         pass
      try:
         f.write(soup[i])
      except:
          pass
<<<<<<< HEAD
################################################


# Below code is a bit bloated, could be cleaned up a bit
=======
####################################################

#below code is a bit bloated, could be cleaned up a bit
>>>>>>> 01616f8e313fa104dd5b05720630c741f8086594
def find_substring_in_list(total, lookingfor, counter):
   counter = counter + 25
   lookingfor = '&count='
   for i in range(len(total)):
      for j in range(len(str(total[i])) - len(lookingfor)):
         x = str(total[i])
         if lookingfor == x[j:j + len(lookingfor)]:
            return total[i]
   print 'Error: No substring in list'

#get the total vote count of all reddit topics on a reddit page
def get_vote_count(target):
   downs = find_indices(target, 'data-downs') # data-downs and data-ups mark where the upvote and downvote count
   ups = find_indices(target, 'data-ups')     # is in the web code
   downvotes = []
   upvotes = []   

for i in range(len(downs)): #Could be optimized
      for j in range(6):
         try:
	    may_be_integer = int(target[downs[i] + 12 + j])                  
         except ValueError:
            downvotes.append(int(target[downs[i] + 12:downs[i] + 12 + j]))
            break
   for i in range(len(ups)):
      for j in range(6):
         try:
	    may_be_integer = int(target[ups[i] + 10 + j])
         except ValueError:
            upvotes.append(int(target[ups[i] + 10:ups[i] + 10 + j]))
            break
   x = []
   for i in range(len(upvotes)):
      x.append(upvotes[i] - downvotes[i])
   return x

#The following three functions are effectively the same: finding the correct
#index of the user and moving around to capture the correct part of what we need

def get_commentlinks(soupyinput):
   global indexme
   returnme = []
   for i in range(25):
      returnme.append(soupyinput[indexme[i] + 1])
   return returnme

def get_hyperlinks(soupyinput):
   global indexme
   returnme = []
   for i in range(25):
      returnme.append(soupyinput[indexme[i] - 2])
   return returnme



def get_users(soupyinput):
   global indexme
   returnme = []
   startpoint = 0
   for i in range(len(soupyinput) - 1):
      if soupyinput[i] == '/about':
         startpoint = i
   for i in range(len(soupyinput) - 1 - startpoint):
      x = str(soupyinput[i + startpoint])
      if len(x) > 26:
         if x[:27] == 'http://www.reddit.com/user/':
            indexme.append(i + startpoint)
            returnme.append(soupyinput[i + startpoint])
   return returnme

<<<<<<< HEAD
# These next two scripts together allow for the link address of the "next" button at the bottom of every subreddit's
# page to be retrieved.
=======
# These next two scripts together allow for the link address of the "next" button at the bottom of every subreddit's page
>>>>>>> 01616f8e313fa104dd5b05720630c741f8086594
def find_index(linklist, findme):
   for i in range(len(linklist)):
      x = find_indices(linklist[i], findme)   
      if len(x) > 2:
         return x
def findnextpage(linklist):
   startme = []
   findme = 'after'
   for i in range(len(linklist)):
      if find_index(linklist[i], findme) != '0':
         return find_index(linklist[i], findme)
<<<<<<< HEAD
   print "FUUUUUUUCK"
   return 4
=======
>>>>>>> 01616f8e313fa104dd5b05720630c741f8086594

# Beginning of retrieving the titles of reddit pages
def get_titles(soupyinput):
   x = index_subst_in_soupy(soupyinput, '<a class="title " href="')
   print x
   return x

<<<<<<< HEAD
# Where the action happens
=======
#where the action happens
>>>>>>> 01616f8e313fa104dd5b05720630c741f8086594
def GetUpvotesOver(webpage, iterations, threshold, oldvotes, oldusers, oldlinks, oldcomments):
   y = 0
   global getusers
   global getvotes
   global getcommentlinks
   global gethyperlinks
   gettitles = []
   hdr = {'User-Agent' : 'RedditDigest Bot'}
   req = Request(webpage, headers=hdr)
   page = urlopen(req)
   stoppingpoint = -1
   soupy = BeautifulSoup(page)
   soup = soupy.prettify()
   linklist = []
   for link in soupy.find_all('a'):
      linklist.append(link.get('href'))
   getusers = oldusers + get_users(linklist) 
   getvotes = oldvotes + get_vote_count(soup)
   getcommentlinks = oldcomments + get_commentlinks(linklist)
   gethyperlinks = oldlinks + get_hyperlinks(linklist)
   nextpage = find_substring_in_list(linklist, '', 0)
   for i in range(25):
      if threshold >= getvotes[i + (25 * iterations)]:   
         if y == 0:
            y = i + (25 * iterations)
      else:
         pass
   returnme = []
   for i in range(y):
      returnme.append((getvotes[i], gethyperlinks[i], getcommentlinks[i], getusers[i]))

   if iterations < 1:
      iterations = iterations + 1
   if y == 0:
      return GetUpvotesOver(nextpage, iterations, threshold, getvotes, getusers, gethyperlinks, getcommentlinks)
   else:
      return returnme

def main():
<<<<<<< HEAD
    global getusers
    global getvotes
    global getcommentlinks
    global gethyperlinks
    global oldtitles
    allthethings = GetUpvotesOver('http://www.reddit.com/r/wtf/top?sort=top&t=day', 0, 1100, [], [], [], [])
=======
    allthethings = GetUpvotesOver('http://www.reddit.com/r/wtf/top?sort=top&t=day', 0, 1300, [], [], [], [])
>>>>>>> 01616f8e313fa104dd5b05720630c741f8086594
    print allthethings

if __name__ == '__main__':
   main()

