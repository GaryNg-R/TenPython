def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todo):
    todos = get_todos()
    todos.append(todo +'\n')
    with open('todos.txt', 'w') as file:
        file.writelines(todos)


def print_todo(todos):
    new_todos = []
    new_todos = [item.strip('\n') for item in todos]


    for i, item in enumerate(new_todos, start = 1):
        print(i, item)

while True: 
    user_action = input("Choose View or Add or Edit or Compelet or  Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("View"):
        todos = get_todos()
        print_todo(todos)
    elif user_action.startswith("Add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo +'\n')
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("Edit"):
        todos = get_todos()
        print_todo(todos)
        number = int(input("Which number you want to edit: "))
        print(number)
        number = number -1 
        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("Compelet"):
        todos = get_todos()
        print_todo(todos)
        number = int(input("Which number you want to edit: "))
        print(number)
        number = number -1 
        todos.pop(number)
        
    elif 'Exit' in user_action:
        break
print("Bye!")
