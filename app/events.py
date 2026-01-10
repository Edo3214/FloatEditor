from pathlib import Path

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
