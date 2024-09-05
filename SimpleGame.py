import PySimpleGUI as sg
from modules.Command_Parsing import command_parser
from modules.Monster_Fight import monster_fight
from modules.Player_Inventory import inventory
from modules.Status import status

# Set up the 'game_state' variable to 'Start'
game_state = 'start'
# A dictionary 'game_places' to store all game places
game_places = {
    'start': {
        'Story': 'You are in the Starting place.\nTo the North is a Forest.\nTo the West is a Grove.',
        'North': 'forest', 
        'South': '', 
        'West': 'grove', 
        'East': '', 
        'Item': '',
        'Image': 'Map/start.png'
    },
    'forest': {
        'Story': 'You are in the Forest.\nTo the North is the Cave.\nTo the South is the Starting place.\nTo the West is River.\nTo the East is Stone.',
        'North': 'cave', 
        'South': 'start', 
        'West': 'river', 
        'East': 'stone', 
        'Item': '',
        'Image': 'Map/forest.png'
    },
    'cave': {
        'Story': 'You arrived a dark cave.\nTo the South is the Forest.',
        'North': '', 
        'South': 'forest', 
        'West': '', 
        'East': '',
        'Item': '',
        'Image': 'Map/cave.png'
    },
    'stone': {
        'Story': 'You came in front of the Stone now.\nTo the West is the Forest.',
        'North': '', 
        'South': '', 
        'West': 'forest', 
        'East': '', 
        'Item': 'medicine',
        'Image': 'Map/stone.png'
    },
    'river': {
        'Story': 'You are by a River.\nTo the East is the Forest.\nTo the South is a Grove.',
        'North': '', 
        'South': 'grove', 
        'West': '', 
        'East': 'forest', 
        'Item': 'gold',
        'Image': 'Map/river.png'
    },
    'grove': {
        'Story': 'You are in a peaceful Grove.\nTo the North is the River.\nTo the East is Starting Place',
        'North': 'river', 
        'South': '', 
        'West': '', 
        'East': 'start', 
        'Item': 'sword',
        'Image': 'Map/grove.png'
    }
}

def show_current_place():
    """
    Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    command_list = 'Use "Go North/South/West/East" to move.\nUse "Status" to check your current status.\nUse "Inventory" to check your inventory.\nUse "pick up" to pick up the item.'
    return game_places[game_state]['Story'] + '\n' + command_list

def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: North, South, West, or East

    Returns:
        string: the story at the current place
    """
    global game_state
    global game_places
    
    current_place = game_places[game_state] # Example: Forest, Cave, Castle
    proposed_state = current_place[direction] # Forest[North] = ''

    if proposed_state == '' :
        return 'You can not go that way.\n' + game_places[game_state]['Story']
    else :
        # Update current place
        game_state = proposed_state 
        # Check if there is a monster in the current place
        monster = monster_fight.encounter_monster(game_state) 
        if monster: # If there is a monster
            monster_prompt = 'There is a monster in the way. \nYou can "Attack" the monster or \n"Run" away.\n'
            return monster_prompt + game_places[game_state]['Story']
        else: # If there is no monster
            return game_places[game_state]['Story']

def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """
    # Window Style
    sg.theme('Dark Blue 3')
    # Input and output
    prompt_input = [sg.Text('Enter your command', font='Helvetica 15', pad=((0, 0), (0, 2))), sg.Input(size=(23, 1), font='Helvetica 12', key='-IN-'), sg.Button('Enter', size=(6,0), bind_return_key=True)]
    command_col = sg.Column([prompt_input])
    # Overall layout
    layout = [
         [sg.Image(r'Map/start.png', size=(500, 500), key="-IMG-"), sg.Text(show_current_place(), size=(100, 10), font='Helvetica 15', key='-OUTPUT-')],
         [command_col]
        ]
    
    return sg.Window('Adventure Game', layout, size=(935, 550))

def process_command(command):
    direction = command_parser.movement_parsing(command) # Call command_parser from 'command_parser.py' to parse the command
    action = command_parser.fighting_parsing(command) # Call command_parser from 'command_parser.py' to parse the command
    current_status = command_parser.status_parsing(command) # Call command_parser from 'command_parser.py' to parse the command
    
    # If the command is not a valid command, set it to a empty string
    current_story = ''

    # Check if the player is dead
    if monster_fight.player['health'] <= 0:
        global game_state
        if command == 'restart':
            # Reset the player and monster health
            monster_fight.player['health'] = 100
            monster_fight.monster_dict['boss']['health'] = 200
            game_state = 'start'
            current_story = 'You have restarted the game.'
        else:
            current_story = 'You are dead!\n Use "restart" to restart the game'
    elif direction:
        # string: the story at the current place
        current_story = game_play(direction.capitalize())
    elif action:
        # Fight with the monster
        current_story = monster_fight.fight(action)
        # Run away from the monster
        if action == "run" and "safe now" in current_story:
            game_state = 'start'
        
        # Pick up the item
        elif action == "pick up":
            item = game_places[game_state]['Item']
            # If there is an item to pick up
            if item:
                # Call add_item function from 'inventory.py' to add the item to the inventory
                pick_up_message = inventory.add_item(item)
                # The item is picked up, so set it to empty
                game_places[game_state]['Item'] = ''
                current_story = pick_up_message + "\n" + game_places[game_state]['Story']
            else:
                current_story = 'There is no item to pick up.' + "\n" + game_places[game_state]['Story']
        
        # Heal the player
        elif action == "heal":
            if "medicine" in inventory.inventory_check():
                monster_fight.player['health'] = 100
                current_story = "You have healed yourself to full health."
            else:
                current_story = "You don't have any medicine to heal yourself."
        
        # Check the inventory
        elif action == "inventory":
            # Call inventory_check function from 'inventory.py' to check the inventory
            current_story = 'This is your inventory:\n' + "\n".join(inventory.inventory_check())

        # Check the current status of the player
    elif current_status:
        player_status = status.check_status()
        current_story = f"This is your current status:\nHealth: {player_status['health']}\nAttack: {player_status['attack']}\nInventory: {player_status['inventory']}"

    # If the command is not a valid command
    else:
        current_story = 'Invalid command, please use \n"North", "South", "West", or "East" to move.'
    
    # Update the image and story of the current place on the window
    window['-IMG-'].update(game_places[game_state]['Image'], size=(500, 500))
    window['-OUTPUT-'].update(current_story)


if __name__ == "__main__":
    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()
    # This is a infinite loop
    while True:
        event, values = window.read()
        print(f'You just trigger {event}')
        command = values['-IN-'].lower().strip()
        if event ==  'Enter': 
            process_command(command) # Call process_command function to process the movement command
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
        else :
            pass
             
    window.close() 