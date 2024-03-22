import subprocess
import sys
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget, QApplication, QLabel, QDialog
import os
import json
import pet


class PetListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('宠物列表')
        layout = QVBoxLayout()

        directory = 'pets'
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.json'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        button = QPushButton(data['name'])
                        button.clicked.connect(lambda _, file_path=file_path: self.show_pet_widget(file_path))
                        layout.addWidget(button)
        self.setLayout(layout)


    def show_pet_widget(self, file_path):
        subprocess.Popen(["python3", "src/pet.py", file_path])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet_list_widget = PetListWidget()
    pet_list_widget.show()
    sys.exit(app.exec_())
