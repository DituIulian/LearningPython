#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d-%m-%Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos, start=1):
            item = item.strip('\n').capitalize()
            print(f"{index}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Invalid input")
            continue
        except IndexError :
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            #Used ANSI code just for the color. Another method is to use " " maybe
            message = f"Todo \033[92m{todo_to_remove}\033[0m has been completed."
            print(message)
        except IndexError :
            print("Invalid input")
            continue
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("exit"):
        break
    else:
       print( "Command is not valid" )

print("Bye")


