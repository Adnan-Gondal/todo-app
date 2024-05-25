def show_todos(filepath="todos.txt"):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.read().splitlines()  # This will remove the newline characters
    return local_todos


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        # Ensure each todo is written with a newline character
        file.writelines(f"{todo}\n" for todo in todos_arg)
