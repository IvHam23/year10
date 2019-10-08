
import requests

'''
def writeHTML(data):
    ofile = open("myapi.html","w")
    ofile.write("<h1>JSON file returned by API call</h1>")
    ofile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    ofile.write(data)
    ofile.close()
'''

myrequest = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=a84871bd877544919555c702318e3536")
datajson = myrequest.json()

ofile = open("Assignment.html","w")
ofile.write("<h1>" + "<u>" + "<c>" + datajson + "</c>" + "</u>" + "</h1>")
ofile.close

'''
def main():
    response = requests.get("https://geo-info.co/43.65,-79.40")
    if (response.status_code == 200):
        data = response.content
        data_as_str = data.decode()
        writeHTML(data_as_str)

        datajson = response.json()
        cities = datajson['nearbyCities']
        for city in cities:
            print(city)
		
    else:
        data = "Error has occured"
        writeHTML(data)

main()
'''
