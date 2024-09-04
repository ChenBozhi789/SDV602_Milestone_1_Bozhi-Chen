def command_parsing(command):
    """
    Parse player command 

    Args:
        command (string): The command entered by player in the input (key='-IN-')

    Returns:
        str: The direction or error information (None)
    """
    directions = ['north', 'south', 'west', 'east'] # Use list to store all directions
    command = command.lower().strip() # Convert to lower and remove all whitespace

    if command.startswith(''):
        direction = command[0:] # Get the copy of direction, start from index 0
    elif command.startswith('Walk to'):
        direction = command[8:] # Get the copy of direction, start from index 8
    elif command.startswith('Move to '):
        direction = command[8:] # Get the copy of direction, start from index 8
    elif command.startswith('go '): # Check if command is a direction
        direction = command[3:] # Get the copy of direction, start from index 3
    else:
        print("Invalid command, please use 'go', 'walk to', or 'move to' to move.\nExample: Go North")
        return None # Return None when player entered command is invalid

    if direction in command:
        return direction
    
    else:
        print("Invalid direction, please use 'North', 'South', 'West', or 'East' to move.\nExample: Go North")
        return None # Return None when player entered direction is invalid

if __name__ == "__main__":
    pass