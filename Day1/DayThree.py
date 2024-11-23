def print_todo(todos):
    new_todos = []
    for item in todos:
        new_todos.append(item.strip("\n"))
    for i, item in enumerate(new_todos, start = 1):
        print(i, item)

while True: 
    user_action = input("Choose View or Add or Edit or Compelet or  Exit: ")
    match user_action.strip():
        case 'View':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            print_todo(todos)
        case 'Add':
            todo = input("add a todo: ")+ '\n'
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'Edit':
            #print_todo()
            edit_input = int(input("Which item you want to edit: "))
            new_todo = input("Enter a new item: ")
            todos[edit_input] = new_todo
            #print_todo()
        case 'Compelet':
            #print_todo()
            compelet_input = int(input("Which item you are compelet "))
            todos.pop(compelet_input-1)
            #print_todo()
        case 'Exit':
            break
print("Bye!")
