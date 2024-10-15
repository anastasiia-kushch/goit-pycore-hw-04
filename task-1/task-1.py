from colorama import Fore, Back
from pathlib import Path

def total_salary(path):
    
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            
        total = 0

        for line in lines:
            try:
                _, salary = line.strip().split(',')
                total += int(salary)
            except ValueError:
                print(Fore.BLACK + Back.MAGENTA + f"Помилка в рядку: {line.strip()} - неправильний формат даних." + Fore.RESET + Back.RESET)
                return None

        average = int(total / len(lines))
        return (total, average)
    
    except FileNotFoundError:
        print(Back.MAGENTA + f"Файл {path} не знайдено." + Back.RESET)
        return None
    except IOError:
        print(Back.MAGENTA + f"Сталася помилка при спробі читання файлу {path}." + Back.RESET)
        return None

path = Path('task-1.txt')            
total, average = total_salary(path)
print(Back.YELLOW + f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}" + Back.RESET)
