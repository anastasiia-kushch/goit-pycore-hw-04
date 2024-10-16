from pathlib import Path
from colorama import Fore, Back

def get_cats_info(path):
    
    '''
    Retrieves information about cats from a specified file.

    Parameters:
    path (str or Path): the path to the text file containing cat data. Each line in the file should represent one cat, with values separated by commas in the format: 'id,name,age'.

    Returns:
    tuple: a tuple of dictionaries, where each dictionary contains the 'id', 'name', and 'age' of a cat.

    Raises:
    ValueError: if there is a formatting error in a line (e.g., missing or incorrect data).
    FileNotFoundError: if the specified file is not found.
    IOError: if there is an error reading the file.

    Note:
    The function prints a detailed error message in case of data format errors or file reading issues. In case of an error, it returns None.
    '''

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        cats_info = tuple()
        
        for line in lines:
            try:
                cat_info = dict()
                id, name, age = line.strip().split(',')
                cat_info['id'] = id
                cat_info['name'] = name
                cat_info['age'] = age
                cats_info += (cat_info,)
            except ValueError:
                print(Back.RED + f"Error in line: {line.strip()} - incorrect data format." + Back.RESET)
                return None
        
        return cats_info
    
    except FileNotFoundError:
        print(Back.RED + f"The file {path} was not found." + Back.RESET)
        return None
    except IOError:
        print(Back.RED + f"An error occurred while trying to read the file {path}." + Back.RESET)
        return None



path = Path('cats.txt')
cats_info = get_cats_info(path)
print(Fore.BLACK + Back.YELLOW + f'{cats_info}' + Fore.RESET + Back.RESET)
