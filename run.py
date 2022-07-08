import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setGeometry(300, 300, 500, 400)

        self.key_values = [['ㅃ', 'ㅉ', 'ㄸ', 'ㄲ', 'ㅆ'],
                        ['ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ'],
                        ['ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ'],
                        ['ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ']]


        self.btn_list = []
        self.btn_top = 450
        self.cnt = 0
        self.create_btn()
        # self.btn = QPushButton("종료", self)
        # self.btn.resize(150,50)
        # self.btn.move(600, 800)
        # self.btn.clicked.connect(self.btn_clicked)
        self.setGeometry(100, 100, 500, 300)
        self.showMaximized()
    
    def btn_clicked(self):
        self.close()
    
    def create_btn(self):
        self.cnt_i = len(self.key_values)
        for i in range(self.cnt_i):
            self.btn_row = []
            self.cnt_j = len(self.key_values[i])
            for j in range(self.cnt_j):
                print(self.key_values[i][j])
                self.btn_row.append(QPushButton(self.key_values[i][j], self))
                self.btn_row[j].resize(QSize(130, 130))
                self.btn_row[j].move(260 + (j * 140), self.btn_top + (i * 140))
                self.btn_row[j].show()
            self.btn_list.append(self.btn_row)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
# button = QPushButton("Button")
# button.show()
app.exec_()