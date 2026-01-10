from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor


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

def move_cursor_to_end(textbox):
    cursor = textbox.textCursor()
    cursor.movePosition(QTextCursor.End)
    textbox.setTextCursor(cursor)