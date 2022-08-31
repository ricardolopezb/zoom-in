import tkinter as tk
import schedule
import pyautogui
import time
import win32gui
import win32.lib.win32con as win32con

# -----------------------------------COSAS PARA HACER-----------------------------

#  -Agregar metadata
#  -Arreglar el tema de la alerta de virus
#  -Poner icono
#  -Hacer un readme con las instrucciones de uso.
#  -Hacer la pagina web de descarga
#  -Cuadrar la reunion para lanzar la beta

##################RESOLUCIONES######################
# -1920x1080  (753, 409)
# -1366x768   (536, 289)
# -3840x2160  (1509, 817)
# -1280x1024  (503, 389)
# -1280x720   (503, 275)

win = tk.Tk()

win.geometry("600x820")
#win.wm_iconbitmap('myicon.ico') #Elegir el directorio
win.title("Zoom In - beta1.0")
#win.state('zoomed')

win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)
win.grid_columnconfigure(3, weight=1)

previous = ""

#----------------------------#####FUNCIONES######----------------------------------
def logIn(id):
    #####   Joining Zoom Meeting   ###################

    #######################################################################################
    #Enter the meeting id as a string here *important that it is in string format
    print("Se activo logIn")
    meet_id = id
    #esc clicked to ensure that the win key will open up correctly in the next step
    pyautogui.press('esc',interval=0.1)

    time.sleep(0.2)

    #these lines are simulating starting up zoom by pressing windows key and typing zoom to open program
    pyautogui.press('win',interval=0.1)
    time.sleep(3)
    pyautogui.write('zoom')
    time.sleep(3)
    pyautogui.press('enter',interval=0.5)


    #time delay to factor for zoom app to load up, good buffer is like 10 sec but its case specific
    time.sleep(10)
    maxed = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(maxed, win32con.SW_MAXIMIZE) # gracias jorji

    #this part simulates clicking join meeting, entering meeting id and pressing enter to join
    ##Make sure the joinButton.png file is located in the same folder as the python file or else it will not work
    ##this tells the script where to click to join the meeting
    time.sleep(3)
    #pyautogui.click(767,371) #buscar como verga maximizarlo
    #EVALUAR LA RESOLUCION DE LA PANTALLA DEL USUARIO:
    # 1 -1920x1080  (753, 409)
    # 2 -1366x768   (536, 289)
    # 3 -3840x2160  (1509, 817)
    # 4 -1280x1024  (503, 389)
    # 5 -1280x720   (503, 275)
    if pyautogui.size() == (1920, 1080):
        pyautogui.click(753,409)
        pyautogui.press('enter',interval=1)

    elif pyautogui.size() == (1366, 768):
        pyautogui.click(536, 289)
        pyautogui.press('enter',interval=1)

    elif pyautogui.size() == (3840, 2160):
        pyautogui.click(1509, 817)
        pyautogui.press('enter',interval=1)

    elif pyautogui.size() == (1280, 1024):
        pyautogui.click(503, 389)
        pyautogui.press('enter',interval=1)

    elif pyautogui.size() == (1280, 720):
        pyautogui.click(503, 275)
        pyautogui.press('enter',interval=1)

    ## the interval of 1 second is important, if not there, then the meeting id will not be inputted
    time.sleep(3)
    pyautogui.write(meet_id)
    pyautogui.press('enter',interval=1)


    # if your meeting has a password then uncomment the code below and enter it here
    # change the value of the variable to your password
    time.sleep(2)
    password = '473632'

    time.sleep(5)
    pyautogui.press('enter',interval=1)
    pyautogui.write(password)
    pyautogui.press('enter',interval = 1)

def cerrarVentana():
    pyautogui.hotkey('alt', 'f4')

def generateSchedule(hora, dia, materia):
    print("Se activo generateSchedule")
    if dia == "Lunes":
        print("Entro al if del dia")
        schedule.every().monday.at(hora).do(logIn, materia)
    elif dia == "Martes":
        print("Entro al if del dia")
        schedule.every().tuesday.at(hora).do(logIn, materia)
    elif dia == "Miercoles":
        print("Entro al if del dia")
        schedule.every().wednesday.at(hora).do(logIn, materia)
    elif dia == "Jueves":
        print("Entro al if del dia")
        schedule.every().thursday.at(hora).do(logIn, materia)
    elif dia == "Viernes":
        print("Entro al if del dia")
        schedule.every().friday.at(hora).do(logIn, materia)


def retrieveSchedule():
    matValue = var.get()
    newId = var3.get()
    matDict["Otro"] = newId
    zoomId = matDict.get(matValue)
    print(matDict)
    diaValue = var1.get()
    horaValue = var2.get()

    print("Se activo retrieveSchedule")
    print("El dia es", diaValue)
    print("La hora es", horaValue)
    print("El id es",zoomId)

    global previous
    stringToDisplay = previous + "\nMateria: " + matValue + " Dia: "+ diaValue + " Hora: " + horaValue
    label_widget['text'] = stringToDisplay
    previous = stringToDisplay
    generateSchedule(horaValue, diaValue, zoomId)

def appearOtro():
    otroLabel.grid(row=9, column=1)
    otroEntry.grid(row=9, column=2)

#----------------------------SECCION "MATERIA"-----------------------------------

materiaLabel = tk.Label(win, text="Materia", pady=12, font="Helvetica 12 bold")

materias = ["Algebra I (Lunes)", "Algebra I (Jueves)", "Analisis I", "Intro a Ing.", "Filosofia", "Quimica", "Otro"]

#----------------------------RADIOBUTTONS DE MATERIAS-----------------------------------
# Cambie los value de ints a sus correspondientes valores de string, para la funcion del log in y schedule
var = tk.StringVar()
R0 = tk.Radiobutton(win, text=materias[0], variable=var, value=materias[0], indicatoron=0, width=16)

R1 = tk.Radiobutton(win, text=materias[1], variable=var, value=materias[1], indicatoron=0, width=16)

R2 = tk.Radiobutton(win, text=materias[2], variable=var, value=materias[2], indicatoron=0, width=16)

R3 = tk.Radiobutton(win, text=materias[3], variable=var, value=materias[3], indicatoron=0, width=16)

R4 = tk.Radiobutton(win, text=materias[4], variable=var, value=materias[4], indicatoron=0, width=16)

R5 = tk.Radiobutton(win, text=materias[5], variable=var, value=materias[5], indicatoron=0, width=16)

R6 = tk.Radiobutton(win, text=materias[6], variable=var, value=materias[6], indicatoron=0, width=16, command=appearOtro)


#--------------------------------------SECCION "DIA"-------------------------------------------------

diaLabel = tk.Label(win, text="Dia", pady=12, font="Helvetica 12 bold") # Esto va a ser una caja con opciones, para seleccionar cada dia.

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

#----------------------------RADIOBUTTONS DE DIAS-----------------------------------
var1 = tk.StringVar()

RD0 = tk.Radiobutton(win, text=dias[0], variable=var1, value=dias[0], indicatoron=0, width=16)

RD1 = tk.Radiobutton(win, text=dias[1], variable=var1, value=dias[1], indicatoron=0, width=16)

RD2 = tk.Radiobutton(win, text=dias[2], variable=var1, value=dias[2], indicatoron=0, width=16)

RD3 = tk.Radiobutton(win, text=dias[3], variable=var1, value=dias[3], indicatoron=0, width=16)

RD4 = tk.Radiobutton(win, text=dias[4], variable=var1, value=dias[4], indicatoron=0, width=16)

#domingo = tk.Radiobutton(win, text="domingo", variable=var1, value="domingo", indicatoron=0, width=16)


#----------------------------------SECCION "HORA"-----------------------------------------------------
var2 = tk.StringVar()
horaLabel = tk.Label(win, text="Hora", pady=12, font="Helvetica 12 bold")

horaEntry = tk.Entry(win, textvariable=var2, width=12)

var3 = tk.StringVar()
otroLabel = tk.Label(win, text="ID (sin espacios):", font="Helvetica 10 bold")
otroEntry = tk.Entry(win, textvariable=var3, width=16)

#------------------------------------DICTIONARY CON CLASES Y U---------------------------------------------------
matDict = {"Algebra I (Lunes)":"998701893", "Algebra I (Jueves)": "225983161", "Analisis I":"730164746", "Intro a Ing.":"818743518", "Filosofia":"727872670", "Quimica":"811928002"}

#-----------------------------------------GENERADOR---------------------------------------------
generador = tk.Button(win, text="Agregar Clase", command=retrieveSchedule, width=20,)

closeButton = tk.Button(win, text="Finalizar Programa", command=cerrarVentana, width=20)

labelframe_widget = tk.LabelFrame(win, text="Clases Logeadas")
label_widget = tk.Label(labelframe_widget, text="")



# ############################ POSICIONES ##############################################
materiaLabel.grid(row=1, column=1)

# Radiobuttons de las materias
R0.grid(row=2, column=1)
R1.grid(row=3, column=1)
R2.grid(row=4, column=1)
R3.grid(row=5, column=1)
R4.grid(row=6, column=1)
R5.grid(row=7, column=1)
R6.grid(row=8, column=1)

diaLabel.grid(row=1, column=3)

# Radiobuttons de Dias
RD0.grid(row=2, column=3)
RD1.grid(row=3, column=3)
RD2.grid(row=4, column=3)
RD3.grid(row=5, column=3)
RD4.grid(row=6, column=3)
labelExtra1 = tk.Label(win, text="").grid(row=10, column=2)

# HORA
horaLabel.grid(row=11, column=2)
hourExplain = tk.Label(win, text="(La hora debe ser ingresada en\nformato HH:MM, de 24hs)", font="Helvetica 9 italic").grid(row=12, column=3)
horaEntry.grid(row=12, column=2)

#idExplain = tk.Label(win, text="(El ID debe ser ingresado\nsin espacios)", font="Helvetica 9 italic")


labelExtra2 = tk.Label(win, text="").grid(row=13, column=2)
# botones
generador.grid(row=14, column=1)
closeButton.grid(row=14, column=3)
labelExtra3 = tk.Label(win, text="").grid(row=15, column=2)
# Label frame
labelframe_widget.grid(row=16, column=2)
label_widget.pack()

########################################################################################
win.mainloop()

while True:
    schedule.run_pending()
    time.sleep(1)
