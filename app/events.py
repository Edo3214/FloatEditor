from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor, QAction
from PySide6.QtWidgets import QFileDialog, QMessageBox


def save_text(textbox, filename="myfile.txt"):
    desktop = Path.home() / "Desktop"
    file_path = desktop / filename
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(textbox.toPlainText())
    print(f"Sačuvano: {file_path}")

def load_text(textbox, filename="myfile.txt"):
    desktop = Path.home() / "Desktop"
    file_path = desktop / filename
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        textbox.setPlainText(content)

def handle_shortcuts(event, textbox):
    if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_S:
        save_text(textbox)
        return True
    elif event.key() == Qt.Key_Escape:
        main_window = textbox.window()
        main_window.showNormal()
        return True
    return False

def handle_shortcuts(event, textbox):
    if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_O:
        save_text(textbox)
        open_file(textbox)
        return True
    return False

def move_cursor_to_end(textbox):
    cursor = textbox.textCursor()
    cursor.movePosition(QTextCursor.End)
    textbox.setTextCursor(cursor)

def initialize_menu_bar(parent):
    menu_bar = parent.menuBar()
    file_menu = menu_bar.addMenu("File")

    new_action = QAction("New", parent)
    new_action.setShortcut("Ctrl+N")
    new_action.triggered.connect(lambda: new_file())
    file_menu.addAction(new_action)

    save_action = QAction("Save", parent)
    save_action.setShortcut("Ctrl+S")
    save_action.triggered.connect(lambda: save_text(parent.textbox))
    file_menu.addAction(save_action)

    save_as_action = QAction("Save as...", parent)
    save_as_action.setShortcut("Ctrl+Shift+S")
    save_as_action.triggered.connect(lambda: save_text_as(parent.textbox))
    file_menu.addAction(save_as_action)

    open_action = QAction("Open file", parent)
    open_action.setShortcut("Ctrl+O")
    open_action.triggered.connect(lambda : open_file(parent.textbox),parent)
    file_menu.addAction(open_action)

    edit_menu = menu_bar.addMenu("Edit")
def new_file():
    print("Not implemented")

def open_file(textbox,parent=None):
    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        "Open File",
        str(Path.home() / "Desktop"),  # default folder
        "Text Files (*.txt);;All Files (*)"  # filter fajlova
    )

    if file_path:  # korisnik nije kliknuo Cancel
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            textbox.setPlainText(content)
            move_cursor_to_end(textbox)
            if parent:
                QMessageBox.information(parent, "Otvoreno", f"Fajl je otvoren:\n{file_path}")
        except Exception as e:
            if parent:
                QMessageBox.critical(parent, "Greška", f"Neuspjelo otvaranje fajla:\n{e}")

def save_text_as(textbox, parent=None):
    # Otvara dijalog za izbor fajla
    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        "Save As",  # naslov dijaloga
        str(Path.home() / "Desktop" / "untitled.txt"),  # default path + ime
        "Text Files (*.txt);;All Files (*)"  # filter fajlova
    )
    if file_path:  # ako korisnik nije kliknuo Cancel
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(textbox.toPlainText())
        QMessageBox.information(parent,"Sacuvano",f"Fajl je sacuvan{file_path}")