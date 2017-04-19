# Note: Uses Python 2.7
# Scrapes a web page and sends a text to your phone using SMTP
# if words indictating a snow day are found. This is made for my districts
# closure page so you may have to adjust the code.

from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
import time
import smtplib
i = 0

server = smtplib.SMTP("smtp.gmail.com:587")  # Use your email smtp 
server.ehlo()
server.starttls()
server.ehlo()
server.login('YOUREMAIL@gmail.com', 'YOURPASSWORD')

BASE_URL = "https://sites.google.com/a/jeffcoschools.us/school-closures/"  # Web page to scrape
      
html = urlopen(str(BASE_URL)).read()
soup = BeautifulSoup(html, "lxml")
info=soup("font")

info = str(info)

closedWords = ['closed', 'following', 'snow', 'delay']
print info

# For 500 minutes (i * 5 == time to run)
while i < 100:
    if closedWords in info:
        msg = "School should be cancelled tomorrow! Please check here to confirm: http://www.jeffcopublicschools.org/closures/"
        server.sendmail("YOUREMAIL@gmail.com", "YOURPHONENUMBER@tmomail.net", msg) 
        i = 101
        server.quit()
        print "Text message sent"
    elif closedWords not in info:
        i = i + 1
        print i
        print "No text sent"
        time.sleep(300)
    else:
        print "else statement called"
