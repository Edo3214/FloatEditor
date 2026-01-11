import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from app.events import *

class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FloatEditor")

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.textbox = QTextEdit()
        layout.addWidget(self.textbox)



        initialize_menu_bar(self)
        self.showMaximized()


    def keyPressEvent(self, event):
        handled = handle_shortcuts(event, self.textbox)
        if not handled:
            super().keyPressEvent(event)
def main():
    app = QApplication(sys.argv)
    window = EditorWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
