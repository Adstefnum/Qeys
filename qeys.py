from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import winsound 

class Keyboard(QMainWindow):
       
   def __init__(self):
    super(Keyboard, self).__init__()
    self.setGeometry(50,50,1080,120)
    self.setWindowTitle("Qeys")
    #self.setWindowIcon(QtGui.QIcon)

    self.piano()
    self.show()

   def piano(self):
    self.whiteKeys(0,65)
    self.whiteKeys(30,73)
    self.whiteKeys(60,82)
    self.whiteKeys(90,87)
    self.whiteKeys(120,98)
    self.whiteKeys(150,110)
    self.whiteKeys(180,123)
    #
    self.whiteKeys(210,130)
    self.whiteKeys(240,146)
    self.whiteKeys(270,164)
    self.whiteKeys(300,174)
    self.whiteKeys(330,196)
    self.whiteKeys(360,220)
    self.whiteKeys(390,246)
    #
    self.whiteKeys(420,260)
    self.whiteKeys(450,292)
    self.whiteKeys(480,328)
    self.whiteKeys(510,348)
    self.whiteKeys(540,392)
    self.whiteKeys(570,440)
    self.whiteKeys(600,492)
    #
    self.whiteKeys(630,520)
    self.whiteKeys(660,584)
    self.whiteKeys(690,656)
    self.whiteKeys(720,696)
    self.whiteKeys(750,784)
    self.whiteKeys(780,880)
    self.whiteKeys(810,984)
    #
    self.whiteKeys(840,1040)
    self.whiteKeys(870,1168)
    self.whiteKeys(900,1312)
    self.whiteKeys(930,1392)
    self.whiteKeys(960,1568)
    self.whiteKeys(990,1760)
    self.whiteKeys(1020,1968)
    self.whiteKeys(1050,2080)

    ##
    self.blackKeys(15,69)
    self.blackKeys(45,78)
    self.blackKeys(105,93)
    self.blackKeys(135,104)
    self.blackKeys(165,117)
    #
    self.blackKeys(225,138)
    self.blackKeys(255,156)
    self.blackKeys(315,186)
    self.blackKeys(345,208)
    self.blackKeys(375,234)
    #
    self.blackKeys(435,276)
    self.blackKeys(465,312)
    self.blackKeys(525,372)
    self.blackKeys(555,416)
    self.blackKeys(585,468)
    #
    self.blackKeys(645,552)
    self.blackKeys(675,624)
    self.blackKeys(735,744)
    self.blackKeys(765,832)
    self.blackKeys(795,936)
    #
    self.blackKeys(855,1104)
    self.blackKeys(885,1248)
    self.blackKeys(945,1488)
    self.blackKeys(975,1664)
    self.blackKeys(1005,1872)

   def whiteKeys(self,x,freq):
    self.y = x
    pianoBtn = QPushButton("",self)
    pianoBtn.resize(40,120)
    pianoBtn.move(x,0)
    pianoBtn.clicked.connect(lambda: winsound.Beep(freq,3))

   def blackKeys(self,x,freq):
    pianoBtn = QPushButton("",self)
    pianoBtn.resize(20,60)
    pianoBtn.setStyleSheet("background-color:black")
    pianoBtn.move(x,0)
    pianoBtn.clicked.connect(lambda: winsound.Beep(freq,3))

   def soundOut(self):
    #download audio and match the key start pos to the keyname and pass that to playsound moduel
    #to play the respective file a = {"0":"C2"}
    #playsound(path_to_audio+a[str(self.y)]+".mp3")
    #set path_to_audio
    soundDict = {"0":"65","1050":"440"}
    print(self.y)
    if str(self.y) in soundDict:
      freq = int(soundDict[str(self.y)])
      print(freq)
      winsound.Beep(freq,4)

app = QApplication(sys.argv)
gui = Keyboard()
sys.exit(app.exec_())