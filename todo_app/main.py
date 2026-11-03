todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for index, item in enumerate(todos):
                item = item.capitalize()
                print(f"{index}. {item}")
        case "edit":
            number = int(input("Enter the todo number you want to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            print("Complete")
        case "exit":
            break
            #Bonus, we might need to delete it later
        case _:
            print("You entered an unknown command: ", user_action)

print("Bye")


