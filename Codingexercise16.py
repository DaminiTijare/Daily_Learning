import PySimpleGUI as st

label=st.Text("Enter feet")
add_input=st.InputText()

label1=st.Text("Enter inches")
add_input1=st.InputText()

convert=st.Button('Convert')

window=st.Window('Convertor',layout=[[label,add_input],
                                     [label1,add_input1]
                                     ,[convert]])
window.read()
window.close()


import PySimpleGUI as sg
 
label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
 
window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                           [option2],
                           [option3],
                           [option4]])
 
window.read()
window.close()
