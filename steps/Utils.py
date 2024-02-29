class Utils():

    def _init_(self, location, imagen):
        self.location=location
        self.imagen=imagen

    def esperarImagen(location, imagen):
        pyautogui.write('ingreso')
        while (location == None):
            try:
                location = pyautogui.locateOnScreen(imagen)
                print("no encuentra")
            except Exception as e:
                print(e)
