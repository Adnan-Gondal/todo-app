from functions import show_todos, write_todos

while True:
    user_action = input("Type add, show, edit,completed or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todos = show_todos()
        todos.append(user_action[4:].capitalize() + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = show_todos()
        for index, item in enumerate(todos):
            print(f"{index + 1}. {item}", end='')

    elif user_action.startswith("edit"):
        try:
            todos = show_todos()
            todo_number = user_action[5:]
            todo_number = int(todo_number) - 1
            new_todo = input("Enter new todo: ") + '\n'

            todos[todo_number] = new_todo

            write_todos(todos)

        except ValueError:
            print("Something is wrong with the command you entered")
            continue

    elif user_action.startswith("completed"):
        try:
            todos = show_todos()

            number = int(user_action[10:])
            index = number - 1
            old_todo = f"Todo {number}: '{todos[index].strip('\n')}' has been deleted"
            todos.pop(index)

            write_todos(todos)

            print(old_todo)

        except IndexError:
            print("There is no entry with this index number")

    elif user_action.startswith("exit"):
        break
    else:
        print("You entered a wrong command")

print("\n\nExiting Program")
