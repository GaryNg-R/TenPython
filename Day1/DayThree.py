todos = []


def print_todo():
    for i, item in enumerate(todos, start = 1):
        print(i, item)

while True: 
    user_action = input("Choose View or Add or Edit or Compelet or  Exit: ")
    match user_action.strip():
        case 'View':
            print_todo()
        case 'Add':
            todo = input("add a todo: ")
            todos.append(todo)
        case 'Edit':
            print_todo()
            edit_input = int(input("Which item you want to edit: "))
            new_todo = input("Enter a new item: ")
            todos[edit_input] = new_todo
            print_todo()
        case 'Compelet':
            print_todo()
            compelet_input = int(input("Which item you are compelet "))
            todos.pop(compelet_input-1)
            print_todo()
        case 'Exit':
            break
print("Bye!")
