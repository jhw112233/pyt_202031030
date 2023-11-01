import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyWin(QWidget):#QWidget 클래스를 상속받는 자식 클래스 선언
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("naver3.png"))#아이콘 넣기
        self.setWindowTitle("나의 메모장")#이름 넣기
        self.move(300,300)#위치 조정
        self.resize(400, 400)#윈도우의 크기
        self.show()# 윈도우 창을 스크린에 보여줌

#if __name__=='__name__': #자동으로 실행안되도록 하는
app = QApplication(sys.argv)
ex = MyWin()
sys.exit(app.exec_())