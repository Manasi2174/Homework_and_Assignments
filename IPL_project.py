# IPL Management System 

# Creating player class
class Players:
    def __init__(self, name, jersey,runs, wickets):
        self.__name = name
        self.__jersey = jersey
        self.__runs = runs
        self.__wickets = wickets
    
    @property
    def name(self): 
        return self.__name
    @property
    def jersey(self):
        return self.__jersey
    
    @property
    def runs(self):
        return self.__runs
    @property
    def wickets(self):
        return self.__wickets

    def all_rounder_score(self):
        return self.__runs>100 and self.wickets>0
    
    def Role_of_player(self):
        return "Bowler" if self.wickets>0 else "Batsman"
    
    def display_info(self):
        print(f"Jersey No: {self.__jersey}, Name: {self.__name}, Runs: {self.__runs}, Wickets:{self.__wickets}")

# Creating Team class
class Teams:
    def __init__(self,nm):
        self.__name=nm
        self.__players=[]

    def get_name(self):
        return self.__name
    
    def add_players(self,player):
        self.__players.append(player)

    def get_players(self):
        return self.__players
    
    def total_runs(self):
        return sum(Players.get_runs() for player in self.__players)
    
    def display_team_info(self):
        print(f"\n Team: {self.__name}")
        for player in self.__players:
            player.display_info()


# creating dictionary for teams and its players
teams_dict={
    "MI":[
        Players("Rohit Sharma",45,runs=418,wickets=0),
        Players("Suryakumar Yadav",63,runs=717, wickets=5),
        Players("Jonny Bairstow", None,runs=85, wickets=0),
        Players("Tilak Varma", 9,runs=343, wickets=0),
        Players("Hardik Pandya", 33,runs=224, wickets=14),
        Players("Naman Dhir", 63,runs=252, wickets=0),
        Players("Mitchell Santner", None, runs=0, wickets=10),
        Players("Jasprit Bumrah ", 93,runs=0, wickets=18),
        Players("Deepak Chahar", 56,runs=0, wickets=11)
    ],
    "CSK":[
        Players("MS Dhoni (wk)", 7, runs=130, wickets=0),
        Players("Ruturaj Gaikwad*", 31, runs=122, wickets=0),
        Players("Devon Conway", 88,runs=156, wickets=0),
        Players("Rahul Tripathi", 52,runs=73, wickets=0),
        Players("Shaik Rasheed", 66, runs=71, wickets=0),
        Players("Ravindra Jadeja", 8, runs=301, wickets=8),
        Players("Ravichandran Ashwin", 99,runs=33, wickets=7),
        Players("Sam Curran", 58,runs=114, wickets=1),
        Players("Matheesha Pathirana", 81, runs=0, wickets=13)
    ],
    "RCB":[
        Players("Virat Kohli", 18, runs=657, wickets=3),
        Players("Phil Salt", 28,runs=403, wickets=0),
        Players("Jitesh Sharma (wk)", 55,runs=261, wickets=0),
        Players("Krunal Pandya", 25,runs=109, wickets=2),
        Players("Bhuvneshwar Kumar", 15,runs=0, wickets=0),
        Players("Yash Dayal", 103,runs=0, wickets=0),
        Players("Romario Shepherd", 16, runs=0, wickets=0),
        Players("Josh Hazlewood", 38, runs=0, wickets=22),
        Players("Mayank Agarwal", 16,runs=0, wickets=0),
        Players("Rajat Patidar", 97,runs=187, wickets=0)
    ]
}

# Show all the teams
for team,players in teams_dict.items():
    print(f"Team: {team}")
    for player in players:
        player.display_info()

print("<------Show Total Runs for each Team------>")
# Display total runs for each team
print(f"Total Runs per Team:")
for team_name,players in teams_dict.items():
    total=sum(player.runs for player in players)
    print(f"{team_name} : {total} Runs")

print("<------Search player by their jersey------->")
jersey_search=eval(input("Enter Jersey number to search : "))
found=False
for team_name,players in teams_dict.items():
    for player in players:
        if player.jersey==jersey_search:
            print(f"Player found in Team :{team_name}")
            found=True

if not found:
    print(f"No player with jersery no {jersey_search} found")
        

print("<-------Role of player based on wickets------>")
for team_name,players in teams_dict.items():
    print(f"Team name : {team_name}")
    for player in players:
        print(f"{player.name} Role -> {player.Role_of_player()}")

print("<--------All Rounder player------->")
for team_name,players in teams_dict.items():
    for player in players:
        if player.all_rounder_score():
            print(f"{player.name} ({team_name}) -> Runs:{player.runs},Wickets :{player.wickets}")









