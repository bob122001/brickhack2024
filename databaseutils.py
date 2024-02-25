from  pymongo import MongoClient
from bson import ObjectId
mongo_client = MongoClient("localhost")
db = mongo_client["lawyercraft"]
games = db['games']
lobbies = db['lobbies']
evidance = db['evidance']


#Lobby Helper functions
def make_lobby():
    lobby = lobbies.insert_one({'player_count':1})
    return str(lobby.inserted_id)

def join_lobby(lobby_id):
    lobby = lobbies.find_one({'_id':ObjectId(lobby_id)})
    if lobby == None:
        return False
    else:
        if lobby['player_count'] < 2:

            lobbies.find_one_and_update({'_id':ObjectId(lobby_id)},{'$set':{'player_count':2}})
            return True
        else:
            return False
    
def get_lobby(lobby_id):
    lobby = lobbies.find_one({'_id':ObjectId(lobby_id)})
    return lobby

def delete_lobby(lobby_id):
    lobby = lobbies.find_one_and_delete({'_id':ObjectId(lobby_id)})
    if lobby == None:
        return False
    else:
        return True

####################################################
    
#Game helper functions
    

def create_game(game_id,story):
    game = games.insert_one({'1':{"money":5000,'cred':0},'game':{'round':0,'story':story},'2':{"money":5000,'cred':0},'lobby_id':game_id})
    return game


def fetch_game(game_id):
    game = games.find_one({'lobby_id':game_id})
    return game


######################################################

#Evidance Helper functions

def fetch_evidance(evidance_id):
    return evidance.find_one({'_id':evidance_id})


######################################################