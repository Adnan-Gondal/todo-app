import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.show_todos(), key="todos", enable_events=True, size=(40, 10))
remove_button = sg.Button("Remove")

layout = [[label], [input_box, add_button], [list_box, sg.Column([[edit_button], [remove_button]])]]

window = sg.Window('My To-Do App', layout=layout, font=("Helvetica", 20))

while True:
    event, value = window.read()
    print("Event happened: ", event, "\n", value)
    if event == "Add":
        todos = functions.show_todos()
        new_todo = value["todo"].strip()
        if new_todo:  # Ensure the new todo is not empty
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=functions.show_todos())
            window["todo"].update(value="")

    elif event == "Edit":
        try:
            selected_todo = value["todos"][0].strip()  # Remove any trailing newlines or spaces
            new_todo = value["todo"].strip()
            if new_todo:  # Ensure the new todo is not empty
                todos = functions.show_todos()
                todo_index = todos.index(selected_todo)
                todos[todo_index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
        except IndexError:
            sg.popup_error("Please select a to-do to edit")
        except ValueError:
            sg.popup_error("Selected to-do not found in the list")

    elif event == "todos":
        window["todo"].update(value=value["todos"][0])

    elif event == "Remove":
        try:
            todos = functions.show_todos()
            selected_todo = value["todos"][0].strip()
            todo_index = todos.index(selected_todo)
            todos.pop(todo_index)
            functions.write_todos(todos)
            window["todos"].update(values=functions.show_todos())

        except IndexError:
            sg.popup_error("Please select a to-do to delete")
        except ValueError:
            sg.popup_error("Selected to-do not found in the list")
        except Exception as e:
            sg.popup_error(f"An unexpected error occurred: {e}")

    elif event == sg.WINDOW_CLOSED:
        break

window.close()
