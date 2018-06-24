# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.parser import parse
import pandas as pd
import requests

class City():
    
    Concerts = []
    eventsLength = 0
    name = ""
    event = ""
    
    def request(self):
        response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?apikey=cfCvyEeFFUCUox7laqXgfSeSX3Ac1zd3&city=" + self.name)
        data = response.json()
        self.eventsLength = len(data["_embedded"]["events"])
        self.venuesLength = len(data["_embedded"]["events"][1]["_embedded"]["venues"])
        self.event = data["_embedded"]["events"]
        
        
    def askForInput(self):
        print("Enter a city:")
        city = input()
        self.name = city
        
    def printConcerts(self):
        k = 0
        for k in range(len(self.Concerts)):
            print()
            print("Name: " + self.Concerts[k].getName())
            print("Date: " + self.Concerts[k].getDate())
            print("Time: " + self.Concerts[k].getTime())
            print("Venue: " + self.Concerts[k].getVenue())
            print()
            
            
    def createEvents(self):
        i = 0
        j = 0
        
        for i in range(self.eventsLength):
            
            for j in range (len(self.event[i]["_embedded"]["venues"])):
                con = Concert()
                con.setName(self.event[i]["name"])
                con.setDate(self.event[i]["dates"]["start"]["localDate"])
                con.setTime(self.event[i]["dates"]["start"]["localTime"])
                con.setVenue(self.event[i]["_embedded"]["venues"][j]["name"])
    
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
        
    def setVenue(self, venue):
        self.venue = venue
    
    def getTime(self):
        return self.time
    
    def getName(self):
        return self.name
    
    def getDate(self):
        return self.date
    
    def getVenue(self):
        return self.venue
        

city = City()
city.request()
city.askForInput()
city.request()
city.createEvents()
city.sortConcerts()
city.printConcerts()


    






