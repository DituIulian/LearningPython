todos = []


while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.capitalize()
                print(item)

        case "edit":
            num = int(input("Enter the todo number you want to edit: "))
            num = num - 1
            new_todo = input("Enter new todo: ")
            todos[num] = new_todo

        case "exit":
            break
            #Bonus, we might need to delete it later
        case _:
            print("You entered an unknown command: ", user_action)

print("Bye")


