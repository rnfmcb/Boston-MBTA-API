#Python program that takes in two stops that are on the same route and can predict the next vehicle that can take you to the second stop. 
from datetime import datetime
import os

# Get the MBTA API key from the system variables. Some places say you don't necessarily need a key. Need to figure out why. 
key = os.environ.get('MBTA_KEY')
url='https://api-v3.mbta.com/'


#Function to ask the api the time the next vehicle will arrive at the first stop, that will travel to the second stop on the route
def getTime(route,stop1,stop2) 
    now = datetime.now() #Get the current time  
    
    #function here using api. I think it is related to 
    # schedules?include=route,trip,stop&filter... includes the routes as well as thttps://www.programiz.com/java-programming/online-compiler/he trips and stops.
    #I would want to get the schedule list of vehicles that fit the 
    #route requirements, then compare "now" to what is next on the list. 
    
return time; 


#Could read in from commandline or a CSV file to get this information.
#For the purposes of this project, gonna ask the user. 
route = input("What is your route?"); 
stop1 = input("What is your first stop"); 
stop2 = input("What is your second stop"); 

time = getTime(route,stop1,stop2); 
print("Time the next vehicle will arrive is:"); 
print(time); 







