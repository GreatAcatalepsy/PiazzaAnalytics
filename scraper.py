from bs4 import BeautifulSoup as bsoup
import requests as rq
import re
import csv
import requests
import urllib2

#page = urllib2.urlopen("https://piazza.com/class/idm78ismocb1jh?cid="+n)
#soup = BeautifulSoup(page)
#metaData = soup.find_all("cid="+n)
#postData = soup.find_all("cid="+n)

base_url = 'https://piazza.com/class/idm78ismocb1jh?'
r = rq.get(base_url)

soup = bsoup(r.text)
page_count_links = soup.find_all("a",href=re.compile(r".*javascript:goToPage.*"))
try: 
    num_post = int(page_count_links[-1].get_text())
except IndexError:
    num_post = 1
	
url_list = ["{}&cid={}".format(base_url, str(page)) for page in range(1, num_post + 1)

views = []
question = []
goodquestion = []
folder = []
studentanswer = []
studthanks = []
instructoranswer = []
instructthanks = []
discussion = []


print "Parsing data..."
for html in metaData:
    text = BeautifulSoup(str(html).strip()).get_text().encode("utf-8").replace("\n", "") 
    views.append(text.split("question")[1].split("views")[0].strip()) 												#get views
    question.append(text.split("views")[1].split("good question")[0].strip()) 										#get question
	goodquestion.append(text.split("good question")[1].split("Updated")[0].strip()) 								#get good question
	folder.append(text.split('\n')[1].split("good question")[0].strip()) 											#get folder
	studentanswer.append(text.split("collectively construct a single answer")[1].split("thanks!")[0].strip())		#get student answer
	studthanks.append(text.split("thanks")[1].split("updated")[0].strip()) 											#get student thanks
	instructoranswer.append(text.split("the instructors' answer,")[1].split("thanks")[0].strip()) 					#get instructor answer
	instructthanks.append(text.split("thanks")[1].split("updated")[0].strip()) 										#get instruct thanks
	discussion.append(text.split("questions and comments")[1].split("Start a new follow-up discussion")[0].strip()) #get discussion

for post in postData:
    posts.append(BeautifulSoup(str(post)).get_text().encode("utf-8").strip())

csvfile = open('piazza225fa15.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(["Views", "Question", "Good Question", "Folder", "Student Answer", "Student Thanks", "Instructor Answer", "Instructor Thanks", "Discussion"])

for views, question, goodquestion, studentanswer, studthanks, instructoranswer, instructthanks, discussion post in zip(views, question, goodquestion, studentanswer, studthanks, instructoranswer, instructthanks, discussion):
    writer.writerow([views, question, goodquestion, studentanswer, studthanks, instructoranswer, instructthanks, discussion])
csvfile.close()