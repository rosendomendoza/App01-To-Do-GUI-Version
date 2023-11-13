PATHFILES = "todos.txt"

def get_todos(filepath=PATHFILES):
    """ Return the list to-do. The default parameter
     for de file name in 'todos.txt '"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=PATHFILES):
    """
    Write in la file the to-do list. return none
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Este codigo se ejecuta como principal")