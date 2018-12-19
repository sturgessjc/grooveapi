
import requests
import json

path = "https://api.groovehq.com/v1/tickets?access_token="
access_token = ""
url = path + access_token


response = requests.get(url)
data = response.text

# Rendering the full api data
parsed = json.loads(data)

# Collecting ticket Data
ticketOneCreated = parsed["tickets"][4]["created_at"]
ticketOneTags = parsed["tickets"][4]["tags"][0]

ticketTwoCreated = parsed["tickets"][4]["created_at"]
ticketTwoTags = parsed["tickets"][4]["tags"][0]

ticketThreeCreated = parsed["tickets"][4]["created_at"]
ticketThreeTags = parsed["tickets"][4]["tags"][0]

ticketFourCreated = parsed["tickets"][4]["created_at"]
ticketFourTags = parsed["tickets"][4]["tags"][0]

ticketFiveCreated = parsed["tickets"][5]["created_at"]
ticketFiveTags = parsed["tickets"][5]["tags"][0]

ticketSixCreated = parsed["tickets"][5]["created_at"]
ticketSixTags = parsed["tickets"][5]["tags"][0]

ticketSevenCreated = parsed["tickets"][6]["created_at"]
ticketSevenTags = parsed["tickets"][6]["tags"][0]

ticketEightCreated = parsed["tickets"][7]["created_at"]
ticketEightTags = parsed["tickets"][7]["tags"][0]

ticketNineCreated = parsed["tickets"][8]["created_at"]
ticketNineTags = parsed["tickets"][8]["tags"][0]

ticketTenCreated = parsed["tickets"][9]["created_at"]
ticketTenTags = parsed["tickets"][9]["tags"][0]

ticketTenCreated = parsed["tickets"][4]["created_at"]
ticketTenTags = parsed["tickets"][4]["tags"][0]

 
# Data added a readable sentence
ticketOne = 'Date Created: ' + ticketOneCreated + ', Ticket Tags: ' + ticketOneTags
ticketTwo = 'Date Created: ' + ticketTwoCreated + ', Ticket Tags: ' + ticketTwoTags
ticketThree = 'Date Created: ' + ticketThreeCreated + ', Ticket Tags: ' + ticketThreeTags
ticketFour = 'Date Created: ' + ticketFourCreated + ', Ticket Tags: ' + ticketFourTags
ticketFive = 'Date Created: ' + ticketFiveCreated + ', Ticket Tags: ' + ticketFiveTags
ticketSix = 'Date Created: ' + ticketSixCreated + ', Ticket Tags: ' + ticketSixTags
ticketSeven = 'Date Created: ' + ticketSevenCreated + ', Ticket Tags: ' + ticketSevenTags
ticketEight = 'Date Created: ' + ticketEightCreated + ', Ticket Tags: ' + ticketEightTags
ticketNine = 'Date Created: ' + ticketNineCreated + ', Ticket Tags: ' + ticketNineTags
ticketTen = 'Date Created: ' + ticketTenCreated + ', Ticket Tags: ' + ticketTenTags


# File containing all the data
dataFile = ticketOne + '\n' + ticketTwo + '\n' + ticketThree + '\n' + ticketFour + '\n' + ticketFive + '\n' + ticketSix + '\n' + ticketSeven + '\n' + ticketEight + '\n' + ticketNine + '\n' + ticketTen

def create():
    f= open("texts.txt", "a+")
    for i in range(10):
        f.write(dataFile)
        f.close()

create()
