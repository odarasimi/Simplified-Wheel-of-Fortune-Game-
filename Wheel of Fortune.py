import random
import sys

#wheel options
#---------------------------------------------------------------------------
wheel = [
    {"type": "cash","text": "$950", "value": 950, "prize": "A trip to Ann Arbor!"},
    {"type": "bankrupt","text": "Bankrupt","prize": False},
    {"type": "loseturn","text": "Lose a turn","prize": False},
    {"type": "cash","text": "$2500","value": 2500,"prize": False},
    {"type": "cash","text": "$900","value": 900,"prize": False},
    {"type": "cash","text": "$700","value": 700,"prize": False},
    {"type": "cash","text": "$600","value": 600,"prize": False},
    {"type": "cash","text": "$800","value": 800,"prize": False},
    {"type": "cash","text": "One Million","value": 1000000,"prize": False},
    {"type": "cash","text": "$650","value": 650,"prize": "A brand new car!"},
    {"type": "cash","text": "900","value": 900,"prize": False},
    {"type": "cash","text": "$700","value": 700,"prize": False},
    {"type": "cash","text": "$600","value": 600,"prize": False}
]
#----------------------------------------------------------------------------
#phrase options
#----------------------------------------------------------------------------
phrases = {
"Fictional Characters": ["Beavis & Butthead","Big Bird Bert & Ernie","Gumby & Pokey","Hansel & Gretel","Jonny Quest & Bandit","Mermaids",
    "Mufasa Simba & Scar","Ren & Stimpy","Rocky & Bullwinkle","The Dynamic Duo","The Hardy Boys","The Simpsons","Tom And Jerry"],
"Family": ["Blythe Danner & Gwyneth Paltrow","Bruce & Laura Dern","Judy Garland & Liza Minelli","Loretta Lynn & Crystal Gayle",
    "Michael & Olympia Dukakis","Naomi Wynonna & Ashley Judd","Tony & Jamie Lee Curtis","Vanessa & Lynn Redgrave","Warren Beatty & Shirley Maclaine",
    "William Stephen & Alec Baldwin"],
"Place": ["Aberdeen Scotland","Adriatic Sea","Aegean Sea","Africa","Albania","Albuquerque New Mexico","Allentown","Amarillo Texas","Amazon Region Of Brazil",
    "Amherst College","Amphitheatre","Amsterdam","Anaheim California","Angola","Anguilla","Appalachia","Arlington Virginia","Armenia","Aruba",
    "Aspen Colorado","Atlanta Georgia","Austria","Babylon","Baghdad","Bakersfield California","Baltimore Maryland","Bangladesh","Bangor Maine",
    "Barbados","Baton Rouge","Bavaria","Beauty Salon","Bedroom","Beijing China","Belgrade","Berkeley California","Bern Switzerland",
    "Bethlehem","Bonn Germany","Borneo","Boston's Fenway Park","Bowling Alley","Brighton England","Brisbane Australia","Bristol England",
    "Brittany France","Broadway","Brown University","Bucharest Romania","Buffalo New York","Bulgaria","Bunker Hill","Burgundy Region Of France",
    "Cairo Egypt","Calcutta India","Cambridge","Camden New Jersey","Cardiff Wales","Castle","Charleston South Carolina","Chicago's Loop","Chile",
    "Chinatown","Classroom","Cleveland Ohio","Clothes Closet","College Dorm","Cologne","Colombia","Columbia University","Copper Mine","Coral Reef",
    "Cornell University","Corvallis Oregon","Country Club","County Seat", "Courtroom","Coventry England","Cycle Shop","Danbury Connecticut","Dartmouth College",
    "Dayton Ohio","Daytona Beach Florida","Dearborn Michigan","Decatur Georgia","Denver","Deserted Island","Disneyland","Djakarta","Dominican Republic",
    "Doorway","Down On The Farm","Downtown","Duluth Minnesota","Dungeon","Durham North Carolina","Dusseldorf","Dwelling","East Hampton Long Island",
    "El Salvador","England","Englewood New Jersey","Erie Canal","Estonia","Eugene Oregon","Europe","Evanston Illinois","Fairfield Connecticut",
    "Fairgrounds","Fairway","Family Farm","Filling Station","Florida Everglades","Fordham University","Formosa","Fort Leavenworth","Frankfort Kentucky",
    "Frankfurt Germany","Freeport Bahamas","Fresno California","Gainesville Florida","Gallup New Mexico","Garage","Gas Station","Genoa Italy","Georgetown",
    "Germany","Gettysburg","Gettysburg National Military Park","Ghana","Gibraltar","Glendale California","Gloucester","Grade School","Granada Spain",
    "Grand Cayman","Great Bear Lake Canada","Great Britain","Greece","Green Room","Grenada","Hamburg Germany","Harbor","Harlem","Harrisburg",
    "Hartford Connecticut","Hattiesburg Mississippi","Heidelberg Germany","Hermosa Beach California","Highway Rest Stop","Hiroshima Japan",
    "Hoboken New Jersey","Holland","Hollywood","Hometown","Hospital","Hotel Room","Hotel Suite","Houston Texas","Hungary","Hunting Lodge",
    "Ice Rink","Iceland","India""Indochina","Inverness Scotland","Irvine California","Italy","Ithaca New York","Jamestown Virginia","Jericho",
    "Joe Robbie Stadium In Miami","Joliet Illinois","Junior High School","Kabul Afghanistan","Key Largo Florida","Key West Florida""Khartoum Sudan",
    "Kuwait","Kyoto Japan","Lafayette Louisiana","Lake Huron","Lake Erie","Lakehurst Naval Air Station","Lancaster","Lansing Michigan","Laredo Texas",
    "Leeds England","Library","Libya","London's Hyde Park","London's Mayfair District","Los Angeles","Los Alamos New Mexico","Lucerne Switzerland",
    "Lyon France",],
"Landmark": ["Acadia National Park","Bermuda's Pink Sand Beaches","Big Bend National Park","Boston Common","Bryce Canyon National Park","Buckingham Palace",
    "Death Valley National Monument","Edison's Home In Menlo Park New Jersey",
    "Ellis Island","Fort Davis National Historic Site","Fort Point National Historic Site","Fort Smith National Historic Site","Glacier National Park",
    "Grand Canyon National Park","Hyde Park National Historic Site","Independence Hall In Philadelphia","India's Ganges River",
    "Jerusalem's Wailing Wall","John Muir National Historic Site","Kings Canyon National Park","Lassen Volcanic National Park","London Bridge",
    "London's Covent Garden","London's Tower Bridge","Mesa Verde National Park","Mount Palomar Observatory","Mount Rushmore","Muir Woods National Monument",
    "Niagara Falls","Panama Canal","Petrified Forest National Park","Piccadilly Circus","Plymouth Rock","Redwood National Park",
    "San Francisco's Fisherman's Wharf","Scotland Yard","Sequoia National Park","Serengeti National Park","Signal Hill National Historic Site",
    "South Carolina's Fort Sumter","Stonehenge","The Eiffel Tower","The Jefferson Memorial","The Lincoln Memorial","The Palace Of Versailles",
    "The Parthenon","The Smithsonian Institution","The Waldorf-Astoria Hotel","The Washington Monument","The White House","The Alamo",
    "The Boston Post Road","The Egyptian Pyramids","The Empire State Building","The Gateway Arch In St. Louis","The Golden Gate Bridge",
    "The Great Wall Of China","The Kremlin In Moscow","The Mission Of San Juan Capistrano","The Rock Of Gibraltar","The Sphinx",
    "The Tower Of London","Thomas Jefferson's Monticello","Tokyo's Ginza District","Valley Forge National Historical Park","Walden Pond","Westminster Abbey",
    "Winchester Cathedral","Windsor Castle"]
    }

#-------------------------------------------------------------------------------------------------------------------------------------------

#Main Player Class
class WOFPlayer:
    #prizeMoney = 0
    #prizes = []
    def __init__(self, name):
        self.name = name 
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt):
        self.prizeMoney += amt
    def goBankrupt(self):
        self.prizeMoney = 0       
    def addPrize(self, prize):
        self.prizes.append(prize)  
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        base_prompt = """
            {} has ${}
            
            Turn for {}
            Category = {}
            Phrase = {}
            Guessed = {}
            
            Guess a letter, phrase, or type 'exit' or 'pass':""".format(self.name, self.prizeMoney, self.name, category, obscuredPhrase, guessed)
        action = input(base_prompt)
        return action
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty
        
    def smartCoinFlip(self):
        value = random.randint(1, 10)
        if value > self.difficulty:
            return True
        else:
            return False
    def getPossibleLetters(self, guessed):
        word = []
        if self.prizeMoney >= 250:
            for item in LETTERS:
                if item not in guessed:
                    word.append(item)
        else:
            for item in LETTERS:
                if item not in guessed and item not in VOWELS:
                    word.append(item)
        return word
                    
    def getMove(self, category, obscuredPhrase, guessed):
        worded = (self.getPossibleLetters(guessed))
        smart = self.smartCoinFlip()
        z = []
        if worded == []:
            return "pass"
        else:
            if smart == True:
                for b in self.SORTED_FREQUENCIES:
                    if b in worded:
                        z.append(b)
                return z[-1]
            else:
                return random.choice(worded)
            

import sys
sys.setExecutionLimit(600000) # let this take up to 10 minutes

import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250


def getNumOfHumanPlayers():
	min = 1
	max = 5
	test = True
	proceed = False
	while test:
		try:
			value = input("Enter number of human players from 1 - 10, or exit to quit the game")
			if value == "exit":
				break
			values = int(value)

			if values < min or values > max:
				print ("input not valid, number must be between 1 - 10")
				test = True
			else:
				valid_value = values
				proceed = True
				test = False
		except ValueError:
			print ("input not valid, enter a number between 1 - 10 for number of human players")
			test = True 
	listOfHumanPlayers = []
	if proceed:
		for item in range(1,valid_value+1):
			playernames = input("Give your name Player{}".format(item))
			playername = WOFHumanPlayer(playernames)
			listOfHumanPlayers.append(playername)

	return listOfHumanPlayers

def getComputer():
	min = 1
	max = 5
	test = True
	proceed = False
	while test:
		try:
			value = input("Enter number of Computer players from 1 - 10, or exit to quit the game")
			if value == "exit":
				break
			values = int(value)

			if values < min or values > max:
				print ("input not valid, number must be between 1 - 10")
				test = True
			else:
				valid_value = values
				proceed = True
				test = False
		except ValueError:
			print ("input not valid, enter a number between 1 - 10 for number of human players")
			test = True 
	listOfCompPlayers = []
	if proceed:
		for item in range(1,valid_value+1):
			playernames = ("Computer{}".format(item))
			diff = int(input("Enter difficulty level for Computer{}".format(item)))
			playername = WOFComputerPlayer(playernames, diff)
			listOfCompPlayers.append(playername)

	return listOfCompPlayers


one = getNumOfHumanPlayers()
two = getComputer()

def getRandomCategoryAndPhrase():
        Category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[Category])
        return (Category, phrase.upper())

Category, phrase = getRandomCategoryAndPhrase()
guessed = []

def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

def showboard(obscurePhrase, guessed, Category):
 	return """
    {} has {}!
 	Category: {}
 	Phrase: {}
 	Guesses: {}""".format(item, item.prizeMoney, Category, obscurePhrase, guessed)

def SpinWheel():
	return random.choice(wheel)

liste = one + two
Play = True
while Play:
    accum = 0
    while accum < len(liste):
        item = liste[accum]
        move = item.getMove(Category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper()
        if move == "EXIT" or move == "PASS":
            Play = False
        else:
            if move not in LETTERS:
                print('Guesses should be letters. Try again.')
                break
            elif move in guessed: # this letter has already been guessed
                print('{} has already been guessed. Try again.'.format(move))
                break
            elif move in VOWELS and item.prizeMoney < VOWEL_COST:
                print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                break
            else:
                guessed.append(move)
                if move in VOWELS:
                    item.prizeMoney -= VOWEL_COST
                accum += 1             
        wheelPrize = SpinWheel()
        if wheelPrize['type'] == 'bankrupt':
            item.goBankrupt()
        elif wheelPrize['type'] == 'loseturn':
            pass
        elif wheelPrize['type'] == 'cash':
            item.prizeMoney += 50
            
        count = phrase.count(move)
        if count > 0:
            if count == 1:
                print("      There is one {}".format(move))
            else:
                print("      There are {} {}'s".format(count, move))
            print(showboard(obscurePhrase(phrase, guessed), guessed, Category))
            item.addMoney(count * wheelPrize['value'])
            if wheelPrize['prize']:
                item.addPrize(wheelPrize['prize'])
            continue
        if accum == len(liste):
            accum = 0
        time.sleep(1)
        if obscurePhrase(phrase, guessed) == phrase:
            Play = False
                
money = []
for ite in liste:
    money.append(ite.prizeMoney)
winner = max(money)    
for iteme in liste:
    if winner == iteme.prizeMoney:
        print ("WINNER IS {}!".format(iteme))
    