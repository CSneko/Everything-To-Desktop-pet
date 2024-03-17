import json
import os
import sys
from PyQt5.QtWidgets import *
import pet

class PetListDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        directory = 'pets'
        self.setWindowTitle('宠物列表')
        layout = QVBoxLayout()

        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.json'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        # 处理宠物数据
                        button = QPushButton(data['name'])
                        button.clicked.connect(lambda: create_pet(file_path))
                        layout.addWidget(button)
        self.setLayout(layout)

class PetDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        directory = 'pets'
        self.setWindowTitle('宠物列表')
        layout = QVBoxLayout()

        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.json'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        # 处理宠物数据
                        button = QPushButton(data['name'])
                        button.clicked.connect(lambda: create_pet(file_path))
                        layout.addWidget(button)
        self.setLayout(layout)

def create_pet(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        if data["type"] == "gif":
            widget = pet.GifWidget(data['path'])

            widget.show()
            sys.exit(app.exec_())
        else:
            print("无效的json")

def create_main_ui():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('主菜单')

    layout = QVBoxLayout()
    button1 = QPushButton('宠物列表')
    button1.clicked.connect(lambda: show_pet_list_dialog())
    layout.addWidget(button1)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())


def show_pet_list_dialog():
    dialog = PetListDialog()
    dialog.exec_()


if __name__ == '__main__':
    create_main_ui()
