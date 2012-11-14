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

def find_indices(target, subst):
   returnme = []
   for i in range(len(target) - len(subst)):
      if target[i:i+len(subst)] == subst:
         returnme.append(i)
   if returnme == []:
      return '0'
   else:      
      return returnme

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

#def index_subst_in_soupy(soupyinput, subst):
#<a class="title " href="
#</a>
#   x = []   
#   for i in range(len(soupyinput)):
#      if subst == soupyinput[i:i+len(subst)]:
#         for j in range(1000):
#            if soupyinput[i + j:i + j + 4] == '</a>':
#               while sou
#   print x
#   return x

def find_substring_in_list(total, lookingfor, counter):
   counter = counter + 25
   lookingfor = '&count='
#  &amp;count=25&amp;after=
#  &count=50&t=week&after=
   for i in range(len(total)):
      for j in range(len(str(total[i])) - len(lookingfor)):
         x = str(total[i])
         if lookingfor == x[j:j + len(lookingfor)]:
            return total[i]
   print 'Error: No substring in list'

#get the total vote count of all reddit topics on a reddit page
def get_vote_count(target):
   downs = find_indices(target, 'data-downs')
   ups = find_indices(target, 'data-ups')
   downvotes = []
   upvotes = []   
   for i in range(len(downs)):
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

#The following three functions are effectively the same; finding the correct
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

#go to the next reddit page

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
   print "FUUUUUUUCK"
   return 4


#   returnme = ''
#   counter = 0
#   a = find_indices(soup, 'nofollow next')
#   print a
#   b = a[0]
#   b = b - 80
#   while returnme == '':
#      b = b - 1
#      if soup[b:b+13] == 'http://www.re':
#         while returnme == '':
#            if soup[b + counter] == '"':
#               returnme = soup[b:b + counter]
#            else:
#               counter = counter + 1
#            if counter > 1000000:
#               print "Problem"
#               break
#      break
#   return returnme

def insert(original, new, pos):
   return original[:pos] + new + original[pos:]


#<a class="title " href="

def get_titles(soupyinput):
   x = index_subst_in_soupy(soupyinput, '<a class="title " href="')
   print x
   return x

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
#   x = findnextpage(soup)
#   print x
   linklist = []
   for link in soupy.find_all('a'):
      linklist.append(link.get('href'))
   getusers = oldusers + get_users(linklist) 
   getvotes = oldvotes + get_vote_count(soup)
   getcommentlinks = oldcomments + get_commentlinks(linklist)
   gethyperlinks = oldlinks + get_hyperlinks(linklist)
#   gettitles = gettitles + get_titles(soup)
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

#      DO THIS
#      newwebpage = NextPage(linklist, webpage, iterations)
#      iterations = iterations + 1
#      GetUpvotesOver(newwebpage, iterations, threshold, getvotes, getusers, gethyperlinks, getcommentlinks)


def main():
    global getusers
    global getvotes
    global getcommentlinks
    global gethyperlinks
    global oldtitles
#   page4 = NextPage('http://www.reddit.com/r/pics/top?sort=top&t=month')
    allthethings = GetUpvotesOver('http://www.reddit.com/r/treecomics/top?sort=top&t=month', 0, 300, [], [], [], [])
    print allthethings
#   webpage = urlopen('http://www.reddit.com/r/hookah/')
#   soupy = BeautifulSoup(webpage)
#   soup = soupy.prettify()
#   print soup
#   votes = get_vote_count(soup)
#   print votes
#   a = []
#   n = 0
#   for link in soupy.find_all('a'):
#      a.append(link.get('href'))
#   print a
#   users = get_users(a)
#   links = get_hyperlinks(a)

if __name__ == '__main__':
   main()

#data-downs
#data-ups

