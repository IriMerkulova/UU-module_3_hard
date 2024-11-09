def calculate_structure_sum(data_structure):
    summer = 0 # Счётчик
    for i in data_structure:
        if isinstance(i, int):
            summer += i
        elif isinstance(i, str):
            summer += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            summer += calculate_structure_sum(i)  # Рекурсивный вызов
        elif isinstance(i, dict):
            summer += sum(len(key) for key in i.keys() if isinstance(key, str)) # Ключи
            summer += calculate_structure_sum(i.values())  # Рекурсивный вызов для значений
    return summer

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)

print(result)
