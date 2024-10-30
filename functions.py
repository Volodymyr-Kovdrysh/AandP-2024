FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a txt file and return list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH ):
    """
    Write the to-do list in the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == '__main__':
    print(get_todos())