from PySide6.QtWidgets import QMainWindow
from UI.Vtn_principal import Ui_VTNWindow
from dominio.Docente import Docente
from dominio.Estudiante import Estudiante


class PersonaPrincipal(QMainWindow):

    def __init__(self):
        super(PersonaPrincipal,self).__init__()
        self.ui = Ui_VTNWindow()
        self.ui.setupUi(self)
        self.ui.stb_menu_barra_estado.showMessage("Bienvenido",2000)
        self.ui.btn_Grabar.clicked.connect(self.grabar)

    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        persona = None
        if tipo_persona == "Docente":
            persona = Docente()
            persona.nombre = self.ui.txt_Nombre.text()
            persona.apellido = self.ui.txt_Apellido.text()
        else:
            persona = Estudiante()
            persona.nombre = self.ui.txt_Nombre.text()
            persona.apellido = self.ui.txt_Apellido.text()

        archivo = None
        try:
            archivo = open("archivo.txt", mode="a")
            archivo.write(persona.__str__())
            archivo.write("\n")
        except Exception as e:
            print("No se pudo grabar")
        finally:
            if archivo:
                archivo.close()
        self.ui.txt_Nombre.setText("")
        self.ui.txt_Apellido.setText("")
        self.ui.stb_menu_barra_estado.showMessage("Grabado con Éxito", 2000)

