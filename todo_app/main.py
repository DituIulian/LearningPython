while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:

        case "add":
            todo = input("Enter a todo: ") + "\n"
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show" | "display":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos, start=1):
                item = item.strip('\n').capitalize()
                print(f"{index}. {item}")

        case "edit":
            number = int(input("Enter the todo number you want to edit: "))
            number = number - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Enter the todo number you want to complete: "))
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} has been completed. "
            print(message)

        case "exit":
            break
            #Bonus, we might need to delete it later
        case _:
            print("You entered an unknown command: ", user_action)

print("Bye")


