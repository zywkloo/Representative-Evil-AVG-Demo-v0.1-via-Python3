#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

import csv
from helper_functions import *
from comp1501_w18_101071022_a4_source import *

#### ====================================================================================================================== ####
#############                                           ROOM_Class                                                 #############
#### ====================================================================================================================== ####

class Room:
    ''' Enemy Class - represents a single Enemy Object. '''
    # Represents common data for all enemies - only loaded once, not per new Enemy (Class Variable)
    map_data = {}
    for room1 in csv_loader("Map.csv"):
        map_data[int(room1[0])] = {"Name": room1[1], 
                                  "Overlook": room1[2],
                                  "Desc": room1[3],
                                  'U':int(room1[4]),
                                  'D':int(room1[5]),
                                  'N':int(room1[6]),
                                  'S':int(room1[7]),
                                  'W':int(room1[8]),
                                  'E':int(room1[9]),
                                  'Ini_loot':room1[10].split(),
                                  'Hint':room1[11],
                                  'Buff':room1[12].split(),
                                  'Buff_Desc':room1[13]}
#No Name    Overlook    Desc    U   D   N   S   W   Ini_Inventory   Hint    Buff    Buff_Desc
                                  
    def __init__(self, room_No):
        self.room_No=room_No,
        self.Name=Room.map_data[room_No]["Name"],
        self.Brief_Desc=Room.map_data[room_No]["Overlook"],
        self.Desc= Room.map_data[room_No]["Desc"],
        self.Dir={'U':Room.map_data[room_No]["U"],
                      'D':Room.map_data[room_No]["D"],
                      'N':Room.map_data[room_No]["N"],
                      'S':Room.map_data[room_No]["S"],
                      'W':Room.map_data[room_No]["W"],
                      'E':Room.map_data[room_No]["E"]},
        self.U=Room.map_data[room_No]["U"],
        self.D=Room.map_data[room_No]["D"],
        self.N=Room.map_data[room_No]["N"],
        self.S=Room.map_data[room_No]["S"],
        self.W=Room.map_data[room_No]["W"],
        self.E=Room.map_data[room_No]["E"],
        self.Hint=Room.map_data[room_No]["Hint"],
        self.Buff_Desc=Room.map_data[room_No]["Buff_Desc"],
        self.Buff=Room.map_data[room_No]["Buff"],
        self.NPC={}  
        #for NPC0 in Enemy.enemy_data:
         # if Enemy.enemy_data[NPC0]['Pos']==room_No:
          #   self.NPC[NPC0]=Enemy(NPC0)     
          # NPC in this room
        self.Items={}  # items in this room