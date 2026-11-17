def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)



while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("files/todos.txt")
        todos.append(todo + "\n")

        write_todos("files/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("files/todos.txt")
        for index, item in enumerate(todos, start=1):
            item = item.strip('\n').capitalize()
            print(f"{index}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("files/todos.txt")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("files/todos.txt", todos)

        except ValueError:
            print("Invalid input")
            continue
        except IndexError :
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos("files/todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("files/todos.txt", todos)
            #Used ANSI code just for the color. Another method is to use " " maybe
            message = f"Todo \033[92m{todo_to_remove}\033[0m has been completed."
            print(message)
        except IndexError :
            print("Invalid input")
            continue
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        break
    else:
       print( "Command is not valid" )

print("Bye")


