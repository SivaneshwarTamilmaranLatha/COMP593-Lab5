""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon
Usage:
  python pokemon_paste.py poke_name
Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    pokemon_info = poke_api.get_pokemon_info(poke_name)
    if pokemon_info is not None:
        title, body_text = get_paste_data(pokemon_info)
        paste_url = pastebin_api.post_new_paste(title, body_text, expiration='1M', listed=False)
        print(paste_url)

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.
    Returns:
        str: Pokemon name
    """
    # Function body
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        print('Error: Pokemon name not provided.')
        sys.exit('Script execution aborted')

def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.
    Args:
        pokemon_info (dict): Dictionary of Pokemon information
    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # Build the paste title
    name = pokemon_info['name'].capitalize()
    title = f'{name}\'s Abilities'

    # Build the paste body text
    body_text = ''
    for ability in pokemon_info['abilities']:
        body_text += ability['ability']['name'].capitalize() + '\n'

    # (title, body_text)
    return title, body_text

if __name__ == '__main__':
    main()