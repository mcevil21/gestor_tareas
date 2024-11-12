from PyQt6 import QtWidgets, QtCore
import sys

# Clase Tarea que representa una tarea con título, descripción y estado de completada
class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

# Clase GestorTareas que maneja la lista de tareas y sus operaciones
class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]


# Clase para la Interfaz Gráfica de Usuario (GUI) usando PyQt6
class GestorTareasGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.gestor = GestorTareas()

    def init_ui(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Gestor de Tareas')
        self.setGeometry(100, 100, 600, 400)

        # Layout principal
        self.layout = QtWidgets.QVBoxLayout(self)

        # Lista de tareas (QListWidget)
        self.lista_tareas = QtWidgets.QListWidget(self)
        self.layout.addWidget(self.lista_tareas)

        # Campos de entrada para título y descripción
        self.titulo_input = QtWidgets.QLineEdit(self)
        self.titulo_input.setPlaceholderText("Título de la tarea")
        self.layout.addWidget(self.titulo_input)

        self.descripcion_input = QtWidgets.QTextEdit(self)
        self.descripcion_input.setPlaceholderText("Descripción de la tarea")
        self.layout.addWidget(self.descripcion_input)

        # Botones para acciones
        self.boton_agregar = QtWidgets.QPushButton("Agregar Tarea", self)
        self.boton_agregar.clicked.connect(self.agregar_tarea)
        self.layout.addWidget(self.boton_agregar)

        self.boton_completar = QtWidgets.QPushButton("Marcar como Completada", self)
        self.boton_completar.clicked.connect(self.marcar_completada)
        self.layout.addWidget(self.boton_completar)

        self.boton_eliminar = QtWidgets.QPushButton("Eliminar Tarea", self)
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)
        self.layout.addWidget(self.boton_eliminar)

    def agregar_tarea(self):
        titulo = self.titulo_input.text()
        descripcion = self.descripcion_input.toPlainText()
        try:
            self.gestor.agregar_tarea(titulo, descripcion)
            self.actualizar_lista_tareas()
            self.titulo_input.clear()
            self.descripcion_input.clear()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def marcar_completada(self):
        item_seleccionado = self.lista_tareas.currentRow()
        if item_seleccionado != -1:
            self.gestor.marcar_completada(item_seleccionado)
            self.actualizar_lista_tareas()

    def eliminar_tarea(self):
        item_seleccionado = self.lista_tareas.currentRow()
        if item_seleccionado != -1:
            self.gestor.eliminar_tarea(item_seleccionado)
            self.actualizar_lista_tareas()

    def actualizar_lista_tareas(self):
        self.lista_tareas.clear()
        for tarea in self.gestor.tareas:
            estado = "[Completada]" if tarea.completada else "[Pendiente]"
            self.lista_tareas.addItem(f"{estado} {tarea.titulo}: {tarea.descripcion}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    gestor_tareas_gui = GestorTareasGUI()
    gestor_tareas_gui.show()
    sys.exit(app.exec())


# Ejecutar la aplicación
if __name__ == "__main__":
    main()
