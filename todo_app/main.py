while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos, start=1):
            item = item.strip('\n').capitalize()
            print(f"{index}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid input")
            continue
        except IndexError :
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} has been completed. "
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
       print( "Command is not invalid" )

print("Bye")


