def get_todos(filepath="files/todos.txt"):
    """ Read a text file and returns a list of to-dos """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """ Write the to-do items list in the text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())