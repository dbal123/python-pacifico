from behave import given, when, then
from pywinauto import Application
import time
import pyautogui 
import pyperclip


@given('el usuario {usuario} inicia sesion en la pagina')
def step_given_monitor_open(context,usuario):

    # utilsElement=Utils()
    rootImages="C:/Users/x11839/Desktop/imagenes desktop/proyecto-pacifico/"
    

    ############ INICIAR SESION ############
    context.app = Application().start("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    # utilsElement.esperarImagen(location,rootImages+'barraNavegador.png')
    location = None
    while (location == None):
        try:
            location = pyautogui.locateOnScreen(rootImages+'barraNavegador.png')
            print(location)
        except Exception as e:
            print(e)
    
    pyautogui.click(rootImages+'barraNavegador.png')
    pyautogui.write('https://cdnacselcert.azureedge.net/')
    pyautogui.press('enter')
    
    location = None
    while (location == None):
        try:
            location = pyautogui.locateOnScreen(rootImages+'linkIniciarSession.png')
            print(location)
        except Exception as e:
            print(e)
      

    pyautogui.click(rootImages+'linkIniciarSession.png')

    location = None
    while (location == None):
        try:
            location = pyautogui.locateOnScreen(rootImages+'usarOtraCuenta.png')
            print(location)
        except Exception as e:
            print(e)
 

    pyautogui.click(rootImages+'usarOtraCuenta.png')

    location = None
    while (location == None):
        try:
            location = pyautogui.locateOnScreen(rootImages+'iniciarSesionSiguiente.png')
            print(location)
        except Exception as e:
            print(e)

    pyautogui.typewrite(usuario)
    pyautogui.hotkey("altright","q")
    pyautogui.typewrite("emeal.nttdata.com")
    pyautogui.click(rootImages+'iniciarSesionSiguiente.png')

    location = None
    while (location == None):
        try:
            location = pyautogui.locateOnScreen(rootImages+'botonIniciarSesion.png')
            print(location)
        except Exception as e:
            print(e)


    pyautogui.write('Damd453%')
     
    pyautogui.moveTo(rootImages+'botonIniciarSesion.png')
    pyautogui.moveRel(-100,-160)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')

    validacionTexto=pyperclip.paste()
    print("Cual es el valor",validacionTexto)
    assert validacionTexto == "sesión"

    location = None
    while (location == None):
        try:
            location = pyautogui.locateOnScreen(rootImages+'botonIniciarSesion.png')
            print(location)
        except Exception as e:
            print(e)



    # time.sleep(5)
    # pyautogui.click(rootImages+'botonIniciarSesion.png')
    
    context.app.kill()
        
    
    


# @when('the user checks the title')
# def step_when_check_title(context):
#     # context.main_window = context.app.Notepad
#     # context.title = context.main_window.Texts()[0]

# @then('the title should be "{expected_title}"')
# def step_then_verify_title(context, expected_title):
#      assert context.title == expected_title, f"Expected title: {expected_title}, Actual title: {context.title}"

# @then('close Notepad')
# def step_then_close_notepad(context):
#     context.app.kill()