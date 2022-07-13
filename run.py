import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from functools import partial


def make_char(i, m, t):
    code = ((i * 21) + m) * 28 + t + 0xAC00
    return chr(code)

def i_chr_idx(cha):
    idx = ((ord(cha) - 0xAC00) // 28) // 21
    return idx

def m_chr_idx(cha):
    idx = ((ord(cha) - 0xAC00) // 28) % 21
    return idx

def t_chr_idx(cha):
    idx = (ord(cha) - 0xAC00) % 28
    return idx

index_i = [
          'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 
          'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 
          'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

index_m = [
          'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 
          'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 
          'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 
          'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ' ]

index_t = [
          '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 
          'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 
          'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

idx_j_comb1 = ['ㄳ','ㄵ','ㄶ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅄ']
idx_j_comb2 = ['ㄱㅅ','ㄴㅈ','ㄴㅎ','ㄹㄱ','ㄹㅁ','ㄹㅂ','ㄹㅅ','ㄹㅌ','ㄹㅍ','ㄹㅎ','ㅂㅅ']
idx_m_comb1 = ['ㅘ','ㅙ','ㅚ','ㅝ','ㅞ','ㅟ','ㅢ']
idx_m_comb2 = ['ㅗㅏ','ㅗㅐ','ㅗㅣ','ㅜㅓ','ㅜㅔ','ㅜㅣ','ㅡㅣ']

ja_code = ord('ㄱ')
ja_code_last = ord('ㅎ')
mo_code = ord('ㅏ')
mo_code_last = ord('ㅣ')


def text_input_event(text_data, cha):

    cha_code = ord(cha)
    is_ja = ja_code <= cha_code and cha_code <= ja_code_last
    is_mo = mo_code <= cha_code and cha_code <= mo_code_last
    
    if text_data:
        last_cha = text_data[-1]
        last_cha_code = ord(last_cha)
        if ja_code <= last_cha_code and last_cha_code <= mo_code_last:
            if ja_code <= last_cha_code and last_cha_code <= ja_code_last:
                if is_mo:
                    i = index_i.index(last_cha)
                    m = index_m.index(cha)
                    t = 0
                    c = make_char(i, m, t)
                    text_data = text_data[:-1] + c
                    return text_data
            elif mo_code <= last_cha_code and last_cha_code <= mo_code_last:
                1
        elif last_cha_code >= 0xAC00 and last_cha_code <= (0xAC00 + 0x2BA4):
            i = i_chr_idx(last_cha)
            m = m_chr_idx(last_cha)
            t = t_chr_idx(last_cha)
            if t == 0:
                if is_ja:
                    if cha in index_t:
                        t = index_t.index(cha)
                        c = make_char(i, m, t)
                        text_data = text_data[:-1] + c
                        return text_data
                elif is_mo:
                    chk_cha = index_m[m] + cha
                    if chk_cha in idx_m_comb2:
                        comb_idx = idx_m_comb2.index(chk_cha)
                        comb_cha = idx_m_comb1[comb_idx]
                        m = index_m.index(comb_cha)
                        c = make_char(i, m, t)
                        text_data = text_data[:-1] + c
                        return text_data
            else:
                if is_mo:
                    t_cha = index_t[t]
                    if t_cha in idx_j_comb1:
                        comb_idx = idx_j_comb1.index(t_cha)
                        part_cha = idx_j_comb2[comb_idx]
                        t = index_t.index(part_cha[0])
                        t_cha = part_cha[1]
                    else:
                        t = 0
                    
                    c1 = make_char(i, m, t)
                    if t_cha in index_i:
                        i = index_i.index(t_cha)
                        m = index_m.index(cha)
                        c2 = make_char(i, m, 0)
                        text_data = text_data[:-1] + c1 + c2
                        return text_data
                elif is_ja:
                    chk_cha = index_t[t] + cha
                    if chk_cha in idx_j_comb2:
                        comb_idx = idx_j_comb2.index(chk_cha)
                        comb_cha = idx_j_comb1[comb_idx]
                        t = index_t.index(comb_cha)
                        c = make_char(i, m, t)
                        text_data = text_data[:-1] + c
                        return text_data
    
    text_data += cha
    return text_data



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('hong!')

        self.text_edit = QTextEdit(self)
        self.text_edit.move(75, 75)
        self.text_edit.resize(1750, 200)
        self.text_edit.setText('')

        self.key_values = [['ㅃ', 'ㅉ', 'ㄸ', 'ㄲ', 'ㅆ'],
                        ['ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ'],
                        ['ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ'],
                        ['ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', ',', '.']]
        
        # self.space_bar = [' ']
        self.enter = ['\n']
        self.row_gap = [0, 0, 0.25, 0.75]
        self.btn_list = []
        self.btn_top = 310
        self.btn_left = 160
        self.cnt = 0
        self.create_btn()
        # self.btn = QPushButton("종료", self)
        # self.btn.resize(150,50)
        # self.btn.move(600, 800)
        # self.btn.clicked.connect(lambda: self.buttonClicked(65))
        self.setGeometry(100, 100, 500, 300)
        self.showMaximized()
    
    def buttonClicked(self, char_ord):
        txt = self.text_edit.toPlainText()

        cha = chr(char_ord)
        # txt += chr(char_ord)
        txt = text_input_event(txt, cha)

        self.text_edit.setText(txt)


    def btn_clicked(self):
        self.close()
    
    def create_btn(self):
        self.cnt_i = len(self.key_values)
        for i in range(self.cnt_i):
            self.btn_row = []
            self.cnt_j = len(self.key_values[i])
            for j in range(self.cnt_j):
                # print(self.key_values[i][j])
                self.btn_row.append(QPushButton(self.key_values[i][j], self))
                self.btn_row[j].resize(QSize(140, 140))
                self.btn_row[j].move(int(self.btn_left + (j * 140) + self.row_gap[i]*140), int(self.btn_top + (i * 140)))
                ham = ord(self.key_values[i][j])
                self.btn_row[j].clicked.connect(partial(self.buttonClicked, ham))
                # print(self.key_values[i][j])
                self.btn_row[j].setFont(QFont('Times', 35))
                self.btn_row[j].show()
            self.btn_list.append(self.btn_row)
        self.space_bar = QPushButton(' ', self)
        self.space_bar.resize(QSize(int(140*6.25), 140))
        self.space_bar.move(int(self.btn_left + 140*2.25), int(self.btn_top + 140*4))
        self.space_bar.clicked.connect(partial(self.buttonClicked, ord(' ')))
        self.space_bar.setFont(QFont('Times', 35))
        self.space_bar.show()
        self.space_bar = QPushButton('Enter', self)
        self.space_bar.resize(QSize(int(140*2), 140))
        self.space_bar.move(int(self.btn_left + 140*9.25), int(self.btn_top + 140*2))
        self.space_bar.clicked.connect(partial(self.buttonClicked, ord('\n')))
        self.space_bar.setFont(QFont('Times', 35))
        self.space_bar.show()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
# button = QPushButton("Button")
# button.show()
app.exec_()