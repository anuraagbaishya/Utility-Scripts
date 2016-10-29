from gi.repository import Notify

from bs4 import BeautifulSoup 
import urllib2
import time
url = "https://cricket.yahoo.com/cricket-live-score-england-vs-bangladesh_194432"
#repace with url of the live match going on
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),'html.parser')

team_name="its "

for team in soup.find_all(class_='name',limit=1):
    print("current team batting derived from yahoo cricket is :")
    team_name=team.get_text()
    print(team.get_text())
curr_score  =  team.get_text()
curr_score  =  curr_score + ' '

while (True):
    


    page=urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(),'html.parser') 
    f=0
    for score in soup.find_all(class_='scr'):
        print("current live score derived from yahoo cricket is :")
        curr_score= curr_score  + score.get_text()
        f=1
    #print(score.get_text())
    # check to bring parser to 0
    if(f==1):
        curr_score=str(curr_score)
    else:
        curr_score=str(0)

    Notify.init("Score")
    Hello=Notify.Notification.new("The score is ", curr_score , "dialog-notification")
    Hello.show()

    #change the time for pop up notifications below
    time.sleep (25.0);
    curr_score  =  team.get_text()
    curr_score  =  curr_score + ' '
