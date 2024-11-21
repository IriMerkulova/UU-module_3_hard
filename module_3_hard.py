def calculate_structure_sum(data_structure):
    summer = 0 # Счётчик
    for i in data_structure:
        if isinstance(i, int) or isinstance(i, float):
            summer += i
        elif isinstance(i, str):
            summer += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            summer += calculate_structure_sum(i)  # Рекурсивный вызов
        elif isinstance(i, dict):
            for key, value in i.items():
                summer += calculate_structure_sum([key, value])
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
