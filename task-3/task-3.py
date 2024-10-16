import sys
from pathlib import Path
from colorama import Fore, Back

def directory_contents(path, level=0):
    """
    Recursively retrieves and prints the contents of a specified directory.

    Parameters:
    path (str or Path): the path to the directory to be visualized. 


    level (int, optional): the current depth level in the directory structure (default is 0). 
                            This is used for indentation in the output.

    Returns:
    None: the function prints the structure of the directory, including subdirectories and files.

    Raises:
    FileNotFoundError: if the specified path does not exist.
    NotADirectoryError: if the specified path is not a directory.
    
    Note:
    The function prints the names of directories prefixed with 📂 and the names of files prefixed with 📜. 
    Errors are printed to the console in red for visibility. 
    This function is intended to be used in conjunction with a command-line interface.
    """

    current_path = Path(path)

    if current_path.is_dir():
        print('  ' * level + Fore.CYAN + f'📂{current_path.name}/' + Fore.RESET)
        for item in current_path.iterdir():
            directory_contents(item, level + 1)
    elif current_path.is_file():
        print('  ' * level + Fore.YELLOW + f'📜{current_path.name}' + Fore.RESET)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]

        try:
            if not Path(directory_path).exists():
                raise FileNotFoundError(f"Path '{directory_path}' not found.")
            if not Path(directory_path).is_dir():
                raise NotADirectoryError(f"'{directory_path}' is not a directory.")
            
            directory_contents(directory_path)

        except FileNotFoundError as e:
            print(Fore.RED + str(e) + Fore.RESET)
        except NotADirectoryError as e:
            print(Fore.RED + str(e) + Fore.RESET)
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}" + Fore.RESET)

    else:
        print(Fore.RED + "Please specify the directory path." + Fore.RESET)
