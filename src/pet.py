import json
import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class GifWidget(QWidget):
    def __init__(self, data):
        super().__init__()
        self.initUI(data)

    def quit(self):
        self.close()
        QApplication.quit()

    def initUI(self, data):
        gif_path = data['path']
        size_x = data['size']['x']
        size_y = data['size']['y']
        speed = data['speed']
        icon = data['icon']

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()

        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setScaledContents(True)  # 设置缩放内容以填充整个空间
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.movie = QMovie(gif_path)
        self.movie.setSpeed(speed)
        self.label.setMovie(self.movie)
        self.movie.start()

        iconpath = os.path.join(icon)
        quit_action = QAction('退出', self, triggered=self.quit)
        quit_action.setIcon(QIcon(iconpath))
        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(quit_action)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(iconpath))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

        self.setFixedSize(size_x, size_y)  # 设置初始窗口大小

    def resizeEvent(self, event):
        size = event.size()
        self.label.setFixedSize(size)  # 在窗口大小变化时，调整 GIF 图片的大小以适应窗口

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    # 获取传入的路径
    path = sys.argv[1]

    with open(path, 'r') as file:
        data = json.load(file)
    pet_type = data['type']
    app = QApplication(sys.argv)
    if pet_type == 'gif':
        widget = GifWidget(data)
    else:
        widget = GifWidget(data)
    widget.show()
    sys.exit(app.exec_())
