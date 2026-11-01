todos = []
number = 1

while True:
    user_action = input("Type add,show or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.capitalize()
                print(number, item)
                number += 1
        case "exit":
            break
            #Bonus, we might need to delete it later
        case _:
            print("You entered an unknown command: ", user_action)

print("Bye")


