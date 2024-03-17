import json
import os
import sys
from PyQt5.QtWidgets import *

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
                        layout.addWidget(button)
        self.setLayout(layout)

def create_main_ui():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('主菜单')

    layout = QVBoxLayout()
    button1 = QPushButton('宠物列表')
    button2 = QPushButton('Button 2')
    button1.clicked.connect(lambda: show_pet_list_dialog())
    layout.addWidget(button1)
    layout.addWidget(button2)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

def show_pet_list_dialog():
    dialog = PetListDialog()
    dialog.exec_()

if __name__ == '__main__':
    create_main_ui()
