from colorama import Fore, Back
from pathlib import Path

def total_salary(path):

    '''
    Calculates the total and average salary of developers from a given file.

    Parameters:
    path (str or Path): The path to the text file containing salary data. Each line in the file should represent one developer, with values separated by commas, in the format: 'name,salary'.

    Returns:
    tuple: A tuple containing two integers - the total salary and the average salary of all developers in the file.

    Raises:
    ValueError: If there is a formatting error in a line (e.g., missing or incorrect salary value).
    FileNotFoundError: If the specified file is not found.
    IOError: If there is an error reading the file.

    Note:
    The function prints a detailed error message in case of data format errors or file reading issues. In case of an error, it returns None.
    '''
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        total = 0

        for line in lines:
            try:
                _, salary = line.strip().split(',')
                total += int(salary)
            except ValueError:
                print(Back.RED + f"Помилка в рядку: {line.strip()} - неправильний формат даних." + Back.RESET)
                return None

        average = int(total / len(lines))
        return (total, average)
    
    except FileNotFoundError:
        print(Back.RED + f"Файл {path} не знайдено." + Back.RESET)
        return None
    except IOError:
        print(Back.RED + f"Сталася помилка при спробі читання файлу {path}." + Back.RESET)
        return None

path = Path('salaries.txt')            
total, average = total_salary(path)
print(Fore.BLACK + Back.YELLOW + f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}" + Back.RESET)
