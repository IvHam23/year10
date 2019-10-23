import requests
from tkinter import *
import webbrowser
from os import path

myrequest = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=a84871bd877544919555c702318e3536")
datajson = myrequest.json()

def writeHTML(datajson,entry):
    myarts = datajson['articles']
    ofile = open("assign1web.html","w")
    ofile.write("<link rel='stylesheet' type='text/css' href='main.css'>")
    ofile.write("<head>" + "<title>Assignment 1</title>" + "</head>")
    ofile.write("<body style='background-color:#e6e6e6;'>" + "<h1>" + "<u>" + "<center>" + "Wall Street Journal Articles for You" + "</center>" + "</u>" + "</h1>" + "</body>")
    ofile.write("<br>")
    ofile.write("<hr>")
    ofile.write("<h3>" + "<p>" + "<u>" + "Recent Articles:" + "</u>" + "<p>" + "</h3>")
    ofile.write("<p>" + "<i>" + "Author - Title - Description" + "</i>" + "</p>")
    ofile.write("<br>")
    ofile.write("<p>" + str(myarts[1]['author']) + " - " + str(myarts[1]['title']) + ":" + str(myarts[1]['description']) + "</p>")
    ofile.write("<p>" + "<u>" + "Read whole article here: " + "</u>" + str(myarts[1]['url']) + "</p>")
    ofile.write("<br>")
    ofile.write("<p>" + str(myarts[2]['author']) + " - " + str(myarts[2]['title']) + ":" + str(myarts[2]['description']) + "</p>")
    ofile.write("<p>" + "<u>" + "Read whole article here: " + "</u>" + str(myarts[2]['url']) + "</p>")
    ofile.write("<br>")
    ofile.write("<p>" + str(myarts[3]['author']) + " - " + str(myarts[3]['title']) + ":" + str(myarts[3]['description']) + "</p>")
    ofile.write("<p>" + "<u>" + "Read whole article here: " + "</u>" + str(myarts[3]['url']) + "</p>")
    ofile.write("<br>")
    ofile.write("<p>" + str(myarts[4]['author']) + " - " + str(myarts[4]['title']) + ":" + str(myarts[4]['description']) + "</p>")
    ofile.write("<p>" + "<u>" + "Read whole article here: " + "</u>" + str(myarts[4]['url']) + "</p>")
    ofile.write("<br>")
    ofile.write("<p>" + str(myarts[5]['author']) + " - " + str(myarts[5]['title']) + ":" + str(myarts[5]['description']) + "</p>")
    ofile.write("<p>" + "<u>" + "Read whole article here: " + "</u>" + str(myarts[5]['url']) + "</p>")
    ofile.write("<br>")
    ofile.write("<br>")
    ofile.write("<br>")
    ofile.write("<h1>" + "Different topics below!" + "</h1>")
    ofile.write("<div class='card'>" + "<img src='https://www.outbrain.com/news/wp-content/uploads/2019/02/Wall-Street-Journal-Logo.png' style='width:100%'>" + "<div class='container'>" + "<h3>" + '<a href="https://www.wsj.com/">Click here to view main page</a>' + "</h3>" + "</div>" + "</div>")
    ofile.write("<div class='card'>" + "<img src='https://pbs.twimg.com/profile_images/587949417577066499/3uCD4xxY.jpg' style='width:100%'>" + "<div class='container'>" + "<h3>" + '<a href="https://www.wsj.com/news/world">Click here to view World</a>' + "</div>" + "</h3>" + "</div>")
    ofile.write("<div class='card'>" + "<img src='https://www.voicesofyouth.org/sites/default/files/images/2019-01/politics3.jpg' style='width:100%'>" + "<div class='container'>" + "<h3>" + '<a href="https://www.wsj.com/news/politics">Click here to view Politics</a>' + "</h3>" + "</div>" + "</div>")
    ofile.write("<div class='card'>" + "<img src='https://davcapadvisors.com/wp-content/uploads/2019/03/stock-market.jpg' style='width:100%'>" + "<div class='container'>" + "<h3>" + '<a href="https://www.wsj.com/news/economy">Click here to view Economy</a>' + "</h3>" + "</div>" + "</div>")
    ofile.write("<div class='card'>" + "<img src='data:image/png;base64,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' style='width:100%'>" + "<div class='container'>" + "<h3>" + '<a href="https://www.wsj.com/news/business">Click here to view Business</a>' + "</h3>" + "</div>" + "</div>")
    ofile.write("<div class='card'>" + "<img src='http://img.caixin.com/2019-07-24/1563971044321649.jpg'>" + "<div class='container'>" + "<h3>" + '<a href="https://www.wsj.com/news/tech">Click here to view Tech</a>' + "</h3>" + "</div>" + "</div>")
    ofile.close

def getAPI():
    myarts = datajson['articles']
    print(str(myarts[1]['title']))
    print(str(myarts[1]['author']))
    print(str(myarts[1]['description']))
    print(str(myarts[1]['url']))
    writeHTML(datajson,entry)
    b2 = Button(root,text="Enter",command=webbrowser.open('file://' + path.realpath('assign1web.html')))
    b2.grid(row=1,column=1)

root = Tk()
root.title("GUI")
root.geometry("425x100")
root.config(background="#b3ffff")

text = Label(root, text="Type a word that you would like to see an article about!", background="#b3ffff")
text.grid(row=0,column=0)   

entry = Entry(root, background="#b3ffff")
entry.grid(row=1,column=0)

button = Button(root, text="Enter",command=getAPI, background="#b3ffff")
button.grid(row=1,column=1)
'''
myarts = datajson['articles']
entry = myarts('title')
if(entry.count('title') > 0):
    print(found)
else:
    print (no)
'''
