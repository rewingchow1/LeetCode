def Parse(component):
    return component


input = {'Task1': {'Task3': {'Task20': 2020}}, 'Task2': 30}
x = input['Task1']['Task3']
print(x)
print(Parse(input))
