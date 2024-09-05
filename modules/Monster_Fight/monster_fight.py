import random
from modules.Player_Inventory import inventory

sword_attack = random.randint(50, 9999)
# Define player and monster
player = {
    'health': 100, 
    'attack': 20
}

monster_dict = {
    'minion': {
        'name': 'Goblin', 
        'health': 100, 
        'attack': 15,
        'drop':'diamond'
    },
    'boss': {
        'name': 'Tiger Pioneer', 
        'health': 200, 
        'attack': 30,
        'drop':'beryl'
    }
}

monster_location = {
    'start': '',
    'forest': 'minion',
    'cave': 'boss',
    'stone': '',
    'river': '',
    'grove': '',
}

global current_monster

def encounter_monster(location):
    """
    Encounter monster in the game

    Args:
        location (str): The location of the monster

    Returns:
        dic: The monster information
    """
    global current_monster
    if monster_location[location] != '':
        # current_monster: minion or boss
        current_monster = monster_dict[monster_location[location]]
        return current_monster
    else:
        return None

def fight(command):
    """
    Fight with the monster

    Args:
        monster (dict): The monster information

    Returns:
        str: The result of the fight
    """
    global monster_dict
    global current_monster
    if command == 'attack':
        # Fighting start
        if current_monster['health'] > 0 and player['health'] > 0:
            # Check if the player has a weapon, if so, add the attack to the player's attack
            if "sword" in inventory.inventory_check():
                player['attack'] += sword_attack
            # Player attack monster
            current_monster['health'] -= player['attack'] 
            # When monster is still alive            
            if current_monster['health'] > 0:
                # Monster health
                monster_health = f"The {current_monster['name']} health: {current_monster['health']}"
                # Monster attack player
                player['health'] -= current_monster['attack'] 
                # Player health: Player is still alive       
                if player['health'] > 0:
                    player_health = f"Your health: {player['health']}"
                # Player health: Player is dead
                if player['health'] <= 0:
                    return 'You are dead!\n Use "restart" to restart the game'
                message = player_health + '\n' + monster_health + "\nUse 'attack' to attack the monster\n again, or use 'run' to run away"  
                return message 
            # When monster is dead, add the drop item to the inventory
            else:
                drop_item = current_monster['drop']
                inventory.add_item(drop_item)
                return f"You have defeated the {current_monster['name']}. \nYou got {drop_item}! \nKeep going!"
    
    # Run away from the monster
    elif command == 'run':
        return "You are safe now \nYou're back in starting position"
    else:
        pass
    
def run():
    pass

if __name__ == "__main__":
    pass