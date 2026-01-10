import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from app.events import *

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()


    # Centralni widget koji drži layout
    central_widget = QWidget()
    layout = QVBoxLayout()

    # Rich textbox
    textbox = QTextEdit()
    layout.addWidget(textbox)
    load_text(textbox)

    # Dugme
    btnSave = QPushButton("Save")
    btnSave.clicked.connect(lambda: save_text(textbox))
    layout.addWidget(btnSave)

    # Primijeni layout na centralni widget
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
