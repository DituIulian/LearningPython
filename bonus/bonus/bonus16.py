import FreeSimpleGUI as sg

label1 = sg.Text("Select file to compress: ")
input1 = sg.Input()
chose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")
window = sg.Window("Compress Files",
                   [[label1, input1, chose_button1],
                    [label2, input2, chose_button2],
                    [compress_button]])
window.read()
window.close()