#Yiwei Zhang 101071022
import math
import csv
import random
from helper_functions import *
from room import *
import sys
#### ====================================================================================================================== ####
#############                                         ENEMY_CLASS                                                  #############
#### ====================================================================================================================== ####

class Enemy:
	enemy_data = {} 
	for enemy in csv_loader("Enemy.csv"):
		enemy_data[int(enemy[0])] = { "Name": enemy[1], 
										"Ini_Resist": int(enemy[2]),
										"Power_Strength": int(enemy[3]),
										'Power_Lore':int(enemy[4]),
										'Power_Charm':int(enemy[5]),
										'Power_Money':int(enemy[6]),
										'Lootchance':int(enemy[7]),
										'Loot':int(enemy[8]),
										'Loot_Money':int(enemy[9]),
										'Loot_NPC':int(enemy[17]),
										'Desc':enemy[10],
										'Brief_Desc':enemy[11],
										'Action':enemy[12],
										'Action0':enemy[13],
										'Pos':enemy[14].split(','),
										'Dialog':enemy[15].split(','),
										'Is_bride':bool(enemy[16])}
#No	Name	ini_resist	Power_Strength	Power_Lore	Power_Charm	Power_Money	Lootchance	Loot	Lootmoney	Desc	Brief_Desc	action	action0	Pos	DialogueIs_bride		
	def __init__(self, Enemy_No):
		self.Enemy_No = int(Enemy_No)
		self.Name = Enemy.enemy_data[Enemy_No]["Name"]
		self.Resist = Enemy.enemy_data[Enemy_No]["Ini_Resist"]
		self.Power_Strength = Enemy.enemy_data[Enemy_No]["Power_Strength"]
		self.Power_Lore = Enemy.enemy_data[Enemy_No]["Power_Lore"]
		self.Power_Charm = Enemy.enemy_data[Enemy_No]["Power_Charm"]
		self.Power_Money = Enemy.enemy_data[Enemy_No]["Power_Money"]
		self.Loot_Item= [Enemy.enemy_data[Enemy_No]["Lootchance"],Enemy.enemy_data[Enemy_No]["Loot"]]
		self.Loot_Money= Enemy.enemy_data[Enemy_No]["Lootmoney"]
		self.Loot_NPC= Enemy.enemy_data[Enemy_No]["Loot_NPC"]
		self.Desc= Enemy.enemy_data[Enemy_No]["Desc"]
		self.Brief_Desc= Enemy.enemy_data[Enemy_No]["Brief_Desc"]
		self.ActionList= Enemy.enemy_data[Enemy_No]["Action"]
		self.Action0= Enemy.enemy_data[Enemy_No]["Action0"]
		self.ActionIndex= 0
		self.ActionCUR= Enemy.enemy_data[Enemy_No]["Action"][0]
		self.PosList= Enemy.enemy_data[Enemy_No]["Pos"]
		self.PosIndex= 0
		self.PosCUR= Enemy.enemy_data[Enemy_No]["Pos"][0]
		self.DialogList= Enemy.enemy_data[Enemy_No]["Dialog"]
		self.DialogIndex= 0
		self.DialogCUR= Enemy.enemy_data[Enemy_No]["Dialog"][0]
		self.Is_bride= Enemy.enemy_data[Enemy_No]["Is_bride"]

	def PushAction(self):
		if self.ActionIndex== 0:
			self.ActionCUR= Enemy.enemy_data[Enemy_No]["Action"][0]
		if  self.ActionIndex<len(self.ActionList)-1:
			self.ActionIndex+= 1
			self.ActionCUR=self.ActionList[ActionIndex]
		else:
			self.ActionIndex= -1
			self.ActionCUR=self.Action0

	def PushPos(self):
		if  self.PosIndex<len(self.PosList)-1:
			self.PosIndex+= 1
			self.PosCUR=self.PosList[PosIndex]
		else:
			self.PosIndex= 0
			self.PosList=self.PosList[::-1]
			self.PosCUR=self.PosList[DialogIndex]  	
	def CheckNextPos(self):
		if len(self.PosList)==1:
			return self.PosList[PosIndex]
		elif self.PosIndex<len(self.PosList)-1:
			return self.PosList[PosIndex+1]
		else:
			return self.PosList[PosIndex-1]
	def PushDialog(self):
		if  self.DialogIndex<len(self.DialogList)-1:
			self.DialogIndex+= 1
			self.DialogCUR=self.DialogList[DialogIndex]
		else:
			self.DialogIndex= 0
			self.DialogCUR=self.DialogList[DialogIndex]  	


#### ====================================================================================================================== ####
#############                                         INITIALIZE                                                   #############
#### ====================================================================================================================== ####


def initialize():
    ''' Initialization function - initializes various aspects of the game including settings, shop, and more.
    Input: None
    Output: game_data dictionary
    '''
    # Initialize the Settings Object
    #settings = Settings()

    # Initialize game_data and return it
    game_data = { "cur_currency": 50,
                  'cur_loc':1,
                  "stay_open": 1,
                  "settings": {},
                  "map": {},
                  "Inventory":{},
                  'hour':0.0 ,
                  'day':1, #current gamelevel object
                  'totalprocess':30,     #next gamelevel int
	              'myself':None,
	              'bag':{}
                  }


    for aroom in Room.map_data:
    	game_data['map'][int(aroom)] = Room(aroom)

    return game_data


#### ====================================================================================================================== ####
#############                                          Helper                                                     #############
#### ====================================================================================================================== ####

def keyand(string,*args):
	liststr=string.lower().split()
	for key in args:
		exsit=False
		for word in liststr:
			if word==key:
				exsit=True
		if exsit==False:
			return False
	return True

def keyor(string,*args):
	liststr=string.lower().split()
	for key in args:
		for word in liststr:
			if word==key:
				return True
	return False

#### ====================================================================================================================== ####
#############                                         UPDATE                                                 #############
#### ====================================================================================================================== ####

#No	Name	Overlook	Desc	U	D	N	S	W	Ini_Inventory	Hint	Buff	Buff_Desc
def process(game_data):
	pass

def update(game_data, curRoom):

	def options(curRoom0):
		optlist=["Instruct","Bag...","Look"]
		for opt in curRoom.Dir[0]:
			if curRoom.Dir[0][opt] is not 0:
				optlist.append('Go '+opt)
		if len(curRoom0.NPC) !=0:
			optlist.append('Contact with...')
		if len(curRoom0.Items) !=0:
			optlist.append('Take Items...')
		return optlist
	def updatetime(game_data, timepast=1):
		if game_data['hour']+timepast>=24:
			if game_data['day']+1>=31:
				game_data['stay_open']=2
				print ('Judgment Day is comming! Prepared to welcome Lora ArcheDemon.')
			else:
				game_data['day']+=1
				game_data['hour']=0
				print ('A new day has begun, some character has moved to another place nearby.')
		else:
			game_data['hour']+=timepast
			print ('You feel a little tired. Unconsciously,'+str(timepast)+' Hour passed.')

	print("##### ====================================================================================================================== ####")
	print("                              #####      Day:"+str(game_data['day']),end="")
	print('    Time:'+str(int(game_data['hour']))+":"+str(int(60*(game_data['hour']-int(game_data['hour']))))+",",end="")
	print("    Judgment Day:"+str(game_data['day'])+"/"+str(game_data['totalprocess'])+"    #####")
	print("##### ====================================================================================================================== ####")
	print("You'are at " +str(curRoom.Name[0])+"." )
	print(curRoom.Brief_Desc[0])
	for NPC0 in curRoom.NPC: 
		print(curRoom.NPC[NPC0].Name+"is standing in the corner.")
	print('----------------------------------------------------------------------------------------------------------------------------------')
	for words in options(curRoom):
		print("  |  ",end='')
		print(words+"  |  ")
	print('----------------------------------------------------------------------------------------------------------------------------------')
	print('Lost Soul: What do you want to do, boy?')
	print('----------------------------------------------------------------------------------------------------------------------------------')
	inp0=input("You :").lower()
	print('----------------------------------------------------------------------------------------------------------------------------------')
	if keyor(inp0,'quit','exit'):
		sys.exit()
	elif keyor(inp0,'look'):
		print("After seriously examiation:",curRoom.Desc)
	elif keyor(inp0,'chat','talk','contact','with'):
		inp1=input("talk with who?")
		for NPC0 in curRoom.NPC: 
			if inp1==curRoom.NPC[NPC0].Name:
				print(curRoom.NPC[NPC0].Name+': What you want to do?')
				inp2=input("Ask 'Who' is that guy? or 'What' you do here?")
				if inp2.lower()=='who':
					print(curRoom.NPC[NPC0].Name+": I'm "+ curRoom.NPC[NPC0].Brief_Desc)
				else :
					print("You:"+curRoom.NPC[NPC0].Desc)
	elif keyor(inp0,'instruct','instruction'):
		print("In this game, you need to find the 10 brides within 30 days. Each action will consume your time. ")
		print("For each day's bigging, some npcs will move around.")
		print("Find as many as you can.Due to heavy course load from 3rd-year courses, the game designer didn't finish the work.")
	elif keyor(inp0,'u','up','d','down','n','north','s','south','w','west','e','east'):
		if keyor(inp0,'u','up') and curRoom.Dir[0]['U'] is not 0:
			game_data['cur_loc']=curRoom.Dir[0]['U'] 
		elif keyor(inp0,'d','down') and curRoom.Dir[0]['D'] is not 0:
			game_data['cur_loc']=curRoom.Dir[0]['D']
		elif keyor(inp0,'n','north') and curRoom.Dir[0]['N'] is not 0:
			game_data['cur_loc']=curRoom.Dir[0]['N']
		elif keyor(inp0,'s','south') and curRoom.Dir[0]['S'] is not 0:
			game_data['cur_loc']=curRoom.Dir[0]['S']
		elif keyor(inp0,'w','west') and curRoom.Dir[0]['W'] is not 0:
			game_data['cur_loc']=curRoom.Dir[0]['W']
		elif keyor(inp0,'e','east') and curRoom.Dir[0]['E'] is not 0:
			game_data['cur_loc']=curRoom.Dir[0]['E']
		updatetime(game_data)
	elif keyor(inp0,'go','pass'):
		print("Lost Soul: Go where, boy? That doesn't sound an available direction.")

	elif keyand(inp0,'lost','soul','ghost'):
		print("Lost Soul: I am a ghost, Obviously, but I cann't remember anything. Please, Please help me to find out what happened to me when I was alive...")
	elif keyor(inp0,'bag','Inventory','bag...'):
		print ("You: you have "+str (game_data["cur_currency"])+ " dollars .")
		if len(game_data["bag"])==0:
			print("You: Except that, you have nothing else.")
	else:
		print("Lost Soul: It doesn't look like anything to me.")

def ending1(game_data):
	print("Belial.The ArchDemon: You didn't collect all brides! Your world is OVER!!!")
def ending2(game_data):
	pass
#### ====================================================================================================================== ####
#############                                       Main Function                                             #############
#### ====================================================================================================================== ####
def main():
    ''' Main function - initializes everything and then enters the primary game loop.
    Input: None
    Output: None
    '''
    # Initialize all required variables and objects
    game_data = initialize()
    #print(game_data['map'][1].Name,Enemy.enemy_data[1]["Name"],game_data['map'][1].Brief_Desc,game_data['map'][1].Hint,game_data['map'][1].Buff)

    # Begin Central Game Loop
    while game_data["stay_open"]!=0:
        if game_data["stay_open"]==1:
            process(game_data)
            update(game_data,game_data['map'][game_data['cur_loc']])
            print ("\n\n\n\n\n")
        elif game_data["stay_open"]==2:
            ending1(game_data)
        elif game_data["stay_open"]==3:
            ending2(game_data)

if __name__ == "__main__":
    main()
