from functions import get_todos, write_todos

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()

        todos.append(todo)

        write_todos(filepath='files/todos.txt', todos_arg=todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your number is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(input('Number of the todo to complete: '))
            todos = get_todos()

            # todo подумати над кращою реалізацію...

            if number < 0:
                print('Your number is not valid')
                continue

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list!"
            print(message)
        except ValueError:
            print('Your number is not valid')
            continue
        except IndexError:
            print('Your index is not valid')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')

print('Babay!')

