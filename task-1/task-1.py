from pathlib import Path

def total_salary(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        
        salaries = tuple()

        for line in lines:
            name, salary = line.strip().split(',')
            print(f'{name} has {salary}')



path = Path('task-1.txt')
total_salary(path)

# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.

# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.