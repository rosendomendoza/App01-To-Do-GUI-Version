import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do",
                         key="todo")
add_button = sg.Button("Add", tooltip="Add Todo")

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete", tooltip="Complete Todo")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=("Helvetica",16))

while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y %H %M %S "))
    #print('event: ', event)
    #print('values: ', values)
    match event:
        case 'Add':
            new_todo = values['todo']
            if new_todo.strip() != "":
                #print("Añadir...")
                todos = functions.get_todos()
                new_todo = new_todo + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            else:
                sg.popup("Enter an item first", font=("Helvetica", 16))

        case 'Edit':
            try:
                #print("Editar...")
                todo_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Select an item first", font=("Helvetica",16))

        case 'Complete':
            try:
                #print("Complete...")
                todo_complete = values['todos'][0]
                todos = functions.get_todos()
                #index = todos.index(todo_complete)
                #todos.pop(index)

                todos.remove(todo_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Select an item first", font=("Helvetica",16))

        case 'Exit':
            break

        case 'todos':
            new_value = values['todos'][0].removesuffix("\n")
            window['todo'].update(value=new_value)
            #print('click')

        case sg.WIN_CLOSED:
            break

print("Goodbye...")

window.close