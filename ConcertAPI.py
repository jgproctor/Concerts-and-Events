# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.parser import parse
import pandas as pd
import requests

class City():
    
    Concerts = []
    length = 0
    name = ""
    event = ""
    
    def request(self):
        response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?apikey=cfCvyEeFFUCUox7laqXgfSeSX3Ac1zd3&city=" + self.name)
        data = response.json()
        self.length = len(data["_embedded"]["events"])
        self.event = data["_embedded"]["events"]
        
        
    def askForInput(self):
        print("Enter a city:")
        city = input()
        self.name = city
        
    def printConcerts(self):
        k = 0
        for k in range(len(self.Concerts)):
            print (self.Concerts[k].getName())
            print (self.Concerts[k].getDate())
            print (self.Concerts[k].getTime())
            print()
            
            
    def createEvents(self):
        i = 0
        
        for i in range(self.length):
    
            con = Concert()
            con.setName(self.event[i]["name"])
            con.setDate(self.event[i]["dates"]["start"]["localDate"])
            con.setTime(self.event[i]["dates"]["start"]["localTime"])
    
            self.Concerts.append(con)

    def sortConcerts(self):
        self.Concerts = sorted(self.Concerts, key = lambda x: datetime.strptime(x.getDate(), '%Y-%m-%d'))

class Concert():
        
    def setTime(self, time):
        self.time = time
        
    def setName(self, name):
        self.name = name
    
    def setDate(self, date):
        self.date = date
    
    def getTime(self):
        return self.time
    
    def getName(self):
        return self.name
    
    def getDate(self):
        return self.date
        

city = City()
city.request()
city.askForInput()
city.request()
city.createEvents()
city.sortConcerts()
city.printConcerts()


    






