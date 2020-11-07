# View -- Graphical Interface including PyQt
from PyQt5 import QtCore, QtGui, QtWidgets


class MainPane(QtWidgets.QWidget):
    def __init__(self, Parent):
        QtWidgets.QWidget.__init__(self)
        self.MainWin = Parent

        MnMnuFont = QtGui.QFont()
        MnMnuFont.setFamily("Bradley Hand")
        MnMnuFont.setPointSize(64)
        MnMnuFont.setBold(True)
#        MnMnuFont.setWeight(75)

        #Main Menu label
        self.lblHeader = QtWidgets.QLabel("Main Menu")
        self.lblHeader.setFont(MnMnuFont)

        HBox1 = QtWidgets.QHBoxLayout()
        HBox1.addStretch(1)
        HBox1.addWidget(self.lblHeader)
        HBox1.addStretch(1)

        ColHdrFont = QtGui.QFont()
        ColHdrFont.setFamily("Bradley Hand")
        ColHdrFont.setPointSize(12)
        ColHdrFont.setBold(True)

        #Create Label for first column
        self.lblColHdr = QtWidgets.QLabel("Technique")
        self.lblColHdr.setFont(ColHdrFont)

        HBox2 = QtWidgets.QHBoxLayout()
        HBox2.addWidget(self.lblColHdr)
        HBox2.addStretch(1)

        #Adding a list to 1st column 2nd row
        self.lswTechs = QtWidgets.QListWidget()
        self.lswTechs.addItem("Lower Beads")
        self.lswTechs.addItem("Mixed Beads")
        self.lswTechs.addItem("+5 Combinations")

        #Adding Button in 2nd column to start program
        self.btnStart = QtWidgets.QPushButton("Start!")
        self.btnStart.clicked.connect(self.SetToProbPane)

        HBox3 = QtWidgets.QHBoxLayout()
        HBox3.addStretch(1)
        HBox3.addWidget(self.btnStart)

        VBox = QtWidgets.QVBoxLayout()
        VBox.addLayout(HBox1)
        VBox.addLayout(HBox2)
        VBox.addWidget(self.lswTechs)
        VBox.addLayout(HBox3)

        self.setLayout(VBox)

    def SetToProbPane(self):
        if(self.lswTechs.currentRow() == 0):
            self.MainWin.SetToProblem()



class WelcomePane(QtWidgets.QWidget):
    def __init__(self, Parent):
        QtWidgets.QWidget.__init__(self)
        self.MainWin = Parent

        #Having welcome text
        self.lblWelcomeText = QtWidgets.QLabel('Welcome to Zoom Breakout Room part 2!')

        #Button for entering portal
        self.btnEnter = QtWidgets.QPushButton("Login")
        self.btnEnter.clicked.connect(self.SetToMainPane)
        
        HBox = QtWidgets.QHBoxLayout()
        HBox.addWidget(self.lblWelcomeText)
        HBox.addStretch(1)

        VBox = QtWidgets.QVBoxLayout()
        VBox.addLayout(HBox)
        VBox.addWidget(self.btnEnter)
        VBox.addStretch(1)
    def SetToMainPane(self):
        self.MainWin.SetThePane(2)    



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #Left=200; 
        #Top=200; 
        Width=800 
        Hight=650
        self.resize(Width, Hight)

        self.NextStkId = 3
        self.StakPanes = {}
        self.StakPanes[1] = WelcomePane(self)
        self.StakPanes[2] = MainPane(self)

        self.CenterPane = self.StakPanes[1]
        self.setCentralWidget(self.CenterPane)

    def SetThePane(self, Id):
        print('Stack Id :',Id)
        if(Id == 2):
            self.CenterPane = MainPane(self)
        else:
            self.CenterPane = self.StakPanes[Id]
        self.setCentralWidget(self.CenterPane)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    App = MainWindow()
    App.show()

    sys.exit(app.exec_())