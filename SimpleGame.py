import PySimpleGUI as sg
from modules.Command_Pasering import command_parser
# from modules.Inventory import inventory
# from modules.Monster_Fight import monster_fight
# from modules.Status import status

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
        'Image': 'start.png'
    },
    'forest': {
        'Story': 'You are in the Forest.\nTo the North is the Cave.\nTo the South is the Starting place.\nTo the West is River.\nTo the East is Stone.',
        'North': 'cave', 
        'South': 'start', 
        'West': 'river', 
        'East': 'stone', 
        'Image': 'forest.png'
    },
    'cave': {
        'Story': 'You arrived at the entrance of a dark cave.\nTo the South is the Forest.',
        'North': '', 
        'South': 'forest', 
        'West': '', 
        'East': '', 
        'Image': 'cave.png'
    },
    'stone': {
        'Story': 'You came in front of the Stone now.\nTo the West is the Forest.',
        'North': '', 
        'South': '', 
        'West': 'forest', 
        'East': '', 
        'Image': 'stone.png'
    },
    'river': {
        'Story': 'You are by a River.\nTo the East is the Forest.\nTo the South is a Grove.',
        'North': '', 
        'South': 'grove', 
        'West': '', 
        'East': 'forest', 
        'Image': 'river.png'
    },
    'grove': {
        'Story': 'You are in a peaceful Grove.\nTo the North is the River.\nTo the East is Starting Place',
        'North': 'river', 
        'South': '', 
        'West': '', 
        'East': 'start', 
        'Image': 'grove.png'
    }
}

def show_current_place():
    """
    Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state

    return game_places[game_state]['Story']

def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South

    Returns:
        string: the story at the current place
    """
    global game_state # Current place
    
    game_place = game_places[game_state] # Example: Forest, Cave, Castle
    proposed_state = game_place[direction] # Forest[North] = ''
    if proposed_state == '' :
        return 'You can not go that way.\n'+game_places[game_state]['Story']
    else :
        game_state = proposed_state # Update current place
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
    prompt_input = [sg.Text('Enter your command', font='Helvetica 15'), sg.Input(size=(23, 1), font='Any 12', key='-IN-'), sg.Button('Enter', size=(6,0), bind_return_key=True)]
    command_col = sg.Column([prompt_input])
    # Overall layout
    layout = [
         [sg.Image(r'start.png', size=(500, 500), key="-IMG-"), sg.Text(show_current_place(), size=(100, 4), font='Helvetica 15', key='-OUTPUT-')],
         [command_col]
        ]
    
    return sg.Window('Adventure Game', layout, size=(820, 550))

if __name__ == "__main__":
    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()
    # This is a infinite loop
    while True:
        event, values = window.read()
        # print(f'You just trigger {event}')
        if event ==  'Enter': 
            current_place = command_parser.command_parsing(values['-IN-']) # Call command_parser from 'command_parser.py' to parse the command
            if 'North'.lower() in current_place:
                current_story = game_play('North')
                window['-OUTPUT-'].update(current_story)
            elif 'South'.lower() in current_place:
                current_story = game_play('South')
                window['-OUTPUT-'].update(current_story)
            elif 'West'.lower() in current_place:
                current_story = game_play('West')
                window['-OUTPUT-'].update(current_story)
            elif 'East'.lower() in current_place:
                current_story = game_play('East')
                window['-OUTPUT-'].update(current_story)
            else:
                window['-OUTPUT-'].update('Invalid direction, please use \n"North", "South", "West", \nor "East" to move.')
            
            window['-IMG-'].update(game_places[game_state]['Image'], size=(500, 500))

        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
        else :
            pass
             
    window.close() 