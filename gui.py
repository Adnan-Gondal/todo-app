import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.show_todos(), key="todos", enable_events=True, size=(40, 10))

window = sg.Window('My To-Do App', layout=[[label],
                                           [input_box, add_button],
                                           [list_box, edit_button]], font=("Helvetica", 20))

while True:
    event, value = window.read()
    print("Event happened: ", event, "\n", value)
    match event:
        case "Add":
            todos = functions.show_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(functions.show_todos())

        case "Edit":
            todo_to_edit = value["todos"][0]
            print(type(todo_to_edit))
            print(todo_to_edit)
            todo_index = functions.show_todos().index(todo_to_edit)
            new_todo = value["todo"]
            todos = functions.show_todos()
            todos[todo_index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)


        case sg.WINDOW_CLOSED:
            break

window.close()
