import sys
import os
import subprocess

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##########################  실행 파일 이름 입력.
filename = "Classifier.py"
##########################

class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setupUI()
		self.setWindowTitle("Montage Generate Application")
		#self.statusBar.showMessage("   Selected Attribute : ")
			
		self.statusBar.move(300,300)
		self.setFixedWidth(900)
		self.setFixedHeight(500)
		
		self.SlideBarState()
		self.statusBar.setStyleSheet("QStatusBar{color:white;font-size:9pt;font-weight:bold;}")
		
	def setupUI(self):
		
		self.setGeometry(500, 200, 900, 500)
		
		oImage = QImage("./test.png")
		sImage = oImage.scaled(QSize(900,500))
		palette = QPalette()
		palette.setBrush(10,QBrush(sImage))
		
		self.setPalette(palette)
		s1label_01 = QLabel("\"SEX\"",self)
		s1label_01.move(630,140)
		s1label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s1label_02 = QLabel("Male",self)
		s1label_02.move(470,155)
		s1label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s1label_03 = QLabel("Female",self)
		s1label_03.move(800,155)
		s1label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s1 = QSlider(Qt.Horizontal, self)
		self.s1.setMinimum(0)
		self.s1.setMaximum(1)
		self.s1.move(510,160)
		self.s1.setValue(0)
		self.s1.setTickPosition(QSlider.TicksBelow)
		self.s1.setTickInterval(0.1)
		self.s1.resize(280,30)
		self.s1.valueChanged.connect(self.SlideBarState)
		#self.checkBox1.setFont(QFont( '',11,))
		
		
		
		s2label_01 = QLabel("\"EYE\"",self)
		s2label_01.move(535,185)
		s2label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s2label_02 = QLabel("Narrow",self)
		s2label_02.move(450,200)
		s2label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s2label_03 = QLabel("Wide",self)
		s2label_03.move(610,200)
		s2label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s2 = QSlider(Qt.Horizontal, self)
		self.s2.setMinimum(0)
		self.s2.setMaximum(2)
		self.s2.move(504,205)
		self.s2.setValue(1)
		self.s2.setTickPosition(QSlider.TicksBelow)
		self.s2.valueChanged.connect(self.SlideBarState)
		self.s2.setTickInterval(0.1)

		
		
		s3label_01 = QLabel("\"NOSE\"",self)
		s3label_01.move(530,235)
		s3label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s3label_02 = QLabel("Small",self)
		s3label_02.move(455,250)
		s3label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s3label_03 = QLabel("Big",self)
		s3label_03.move(610,250)
		s3label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s3 = QSlider(Qt.Horizontal, self)
		self.s3.setMinimum(0)
		self.s3.setMaximum(2)
		self.s3.move(504,255)
		self.s3.setValue(1)
		self.s3.setTickPosition(QSlider.TicksBelow)
		self.s3.valueChanged.connect(self.SlideBarState)
		self.s3.setTickInterval(0.1)

		
		s4label_01 = QLabel("\"LIPS\"",self)
		s4label_01.move(530,285)
		s4label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s4label_02 = QLabel("Small",self)
		s4label_02.move(455,300)
		s4label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s4label_03 = QLabel("Big",self)
		s4label_03.move(610,300)
		s4label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s4 = QSlider(Qt.Horizontal, self)
		self.s4.setMinimum(0)
		self.s4.setMaximum(2)
		self.s4.move(504,305)
		self.s4.setValue(1)
		self.s4.setTickPosition(QSlider.TicksBelow)
		self.s4.valueChanged.connect(self.SlideBarState)
		self.s4.setTickInterval(0.1)

		
		""" NO LABEL HERE """
		self.s5label_01 = QLabel("",self)
		self.s5label_01.move(715,185)
		self.s5label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s5label_02 = QLabel("YES",self)
		s5label_02.move(668,200)
		s5label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s5label_03 = QLabel("NO",self)
		s5label_03.move(816,200)
		s5label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s5 = QSlider(Qt.Horizontal, self)
		self.s5.setMinimum(0)
		self.s5.setMaximum(1)
		self.s5.move(705,205)
		self.s5.setValue(0)
		self.s5.setTickPosition(QSlider.TicksBelow)
		self.s5.valueChanged.connect(self.SlideBarState)
		self.s5.setTickInterval(0.1)

		
		
		s6label_01 = QLabel("\"AGE\"",self)
		s6label_01.move(730,235)
		s6label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s6label_02 = QLabel("Young",self)
		s6label_02.move(655,250)
		s6label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s6label_03 = QLabel("Old",self)
		s6label_03.move(816,250)
		s6label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s6 = QSlider(Qt.Horizontal, self)
		self.s6.setMinimum(0)
		self.s6.setMaximum(2)
		self.s6.move(705,255)
		self.s6.setValue(1)
		self.s6.setTickPosition(QSlider.TicksBelow)
		self.s6.valueChanged.connect(self.SlideBarState)
		self.s6.setTickInterval(0.1)
	
		
		
		s7label_01 = QLabel("\"GLASSES\"",self)
		s7label_01.move(712,285)
		s7label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s7label_02 = QLabel("YES",self)
		s7label_02.move(668,300)
		s7label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s7label_03 = QLabel("NO",self)
		s7label_03.move(816,300)
		s7label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s7 = QSlider(Qt.Horizontal, self)
		self.s7.setMinimum(0)
		self.s7.setMaximum(2)
		self.s7.move(705,305)
		self.s7.setValue(1)
		self.s7.setTickPosition(QSlider.TicksBelow)
		self.s7.valueChanged.connect(self.SlideBarState)
		self.s7.setTickInterval(0.1)
	
		
		s8label_01 = QLabel("\"RACE\"",self)
		s8label_01.move(625,330)
		s8label_01.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s8label_02 = QLabel("White",self)
		s8label_02.move(465,345)
		s8label_02.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		s8label_03 = QLabel("Black",self)
		s8label_03.move(800,345)
		s8label_03.setStyleSheet("QLabel{color:white;font-size:9pt;font-weight:bold;}")
		self.s8 = QSlider(Qt.Horizontal, self)
		self.s8.setMinimum(0)
		self.s8.setMaximum(1)
		self.s8.move(510,350)
		self.s8.setValue(1)
		self.s8.setTickPosition(QSlider.TicksBelow)
		self.s8.setTickInterval(0.1)
		self.s8.resize(280,30)
		self.s8.valueChanged.connect(self.SlideBarState)
		#self.checkBox1.setFont(QFont( '',11,))

		Initializebutton = QPushButton("Initialize(&I)" ,self)
		Initializebutton.move(470,400)
		Initializebutton.clicked.connect(self.Initialize_clicked)
		
		Launchbutton = QPushButton("Launch(&L)",self)
		Launchbutton.move(600,400)
		Launchbutton.setAutoDefault(True)
		Launchbutton.clicked.connect(self.Launchbutton_clicked)
		
		Exitbutton = QPushButton("Close(&C)" ,self)
		Exitbutton.move(730,400)
		Exitbutton.clicked.connect(self.Exitbutton_clicked)
		
		self.statusBar = QStatusBar(self)
		self.setStatusBar(self.statusBar)
		

		
	def Initialize_clicked(self):
		self.s1.setValue(0)
		self.s2.setValue(1)
		self.s3.setValue(1)
		self.s4.setValue(1)
		self.s5.setValue(0)
		self.s6.setValue(1)
		self.s7.setValue(1)
		self.s8.setValue(0)
	
	def Launchbutton_clicked(self):
		#os.system("start")
		#os.system(self.cmd)
		os.system("python3 " + filename + " " + self.cmd)
		print(self.msg)
		#ex.runcommand()


	def Exitbutton_clicked(self):
		exit()
		
	def SlideBarState(self):
		self.cmd = ""
		self.msg = " Selected Attribute = "
		self.Cond = ""
		if self.s1.value() == 0:
			self.msg += "Male "
			self.cmd += "10"
			self.s5label_01.setText("\"Mustache\"")
			self.s5label_01.move(715,185)
		if self.s1.value() == 1:
			self.msg += "FeMale "
			self.cmd += "01"
			self.s5label_01.setText("\"High_Cheek\"")
			self.s5label_01.move(710,185)
			
		if self.s2.value() == 0:
			self.msg += ", Narrow_EYE"
			self.cmd += "10"
		if self.s2.value() == 1:
			self.msg += ""
			self.cmd += "00"
		if self.s2.value() == 2:
			self.msg += ", Wide_EYE"
			self.cmd += "01"
			
		if self.s3.value() == 0:
			self.msg += ", Small_Nose"
			self.cmd += "10"
		if self.s3.value() == 1:
			self.msg += ""
			self.cmd += "00"
		if self.s3.value() == 2:
			self.msg += ", Big_Nose "
			self.cmd += "01"
			
		if self.s4.value() == 0:
			self.msg += ", Small_Lips "
			self.cmd += "10"
		if self.s4.value() == 1:
			self.msg += ""
			self.cmd += "00"
		if self.s4.value() == 2:
			self.msg += ", Big_Lips"
			self.cmd += "01"
			
		if self.s1.value() == 0:
			if self.s5.value() == 0:
				self.msg += ", Beard"
				self.cmd += "10"
			if self.s5.value() == 1:
				self.msg += ", No_Beard"
				self.cmd += "00"
		if self.s1.value() == 1:
			if self.s5.value() == 0:
				self.msg += ", High_Cheek"
				self.cmd += "01"
			if self.s5.value() == 1:
				self.msg += ", Normal_Cheek"
				self.cmd += "00"
			
		if self.s6.value() == 0:
			self.msg += ", Young"
			self.cmd += "10"
		if self.s6.value() == 1:
			self.msg += ""
			self.cmd += "00"			
		if self.s6.value() == 2:
			self.msg += ", Old"
			self.cmd += "01"
			
		if self.s7.value() == 0:
			self.msg += ", Glasses"
			self.cmd += "10"
		if self.s7.value() == 1:
			self.msg += ""
			self.cmd += "00"
		if self.s7.value() == 2:
			self.msg += ", No_Glasses"
			self.cmd += "01"
			
		if self.s8.value() == 0:
			self.msg += ", White "
			self.cmd += "10"
		if self.s8.value() == 1:
			self.msg += ", Black "
			self.cmd += "01"
					

		
		self.statusBar.showMessage(self.msg)

"""
class runcommands(QWidget):
	def __init__(self, parent=None):
		super(runcommands, self).__init__(parent)
		self.setGeometry(500, 750, 900, 100)
		layout = QFormLayout()
		self.table = QTableWidget()
		self.table.setColumnCount(5)
		self.param = Mainwindow.cmd
		self.model = QStandardItemModel()
		self.table.setHorizontalHeaderLabels(['Process','Parameter','StdOut', 'Status', 'Kill'])
		self.rowcount = 0
		layout.addRow(self.table)
		self.setLayout(layout)
		self.setWindowTitle("Process Management")
		self.commandrunning=0
		self.mylistofprocesses=[]


	def runcommand(self):
        # add a record in the QTableWidget
        # updating its row number at each run
		self.rowcount = self.rowcount + 1
		self.table.setRowCount(self.rowcount)

        # add column 0: command string
		self.c1 = QTableWidgetItem()
		self.c1.setText(os.getcwd() +'\\'+ " *.py")
		self.table.setItem(self.rowcount - 1, 0, self.c1)

        # add column 1: parameter string
		self.c2 = QTableWidgetItem()
		self.c2.setText(Mainwindow.cmd)
		self.table.setItem(self.rowcount - 1, 1, self.c2)

        # add column 2 to store the  Process StandardOutput
		stdout_item = QTableWidgetItem()
		self.table.setItem(self.rowcount - 1, 2, stdout_item)

        # add column 3: index to store the process status (0: Not Running, 1: Starting, 2: Running)
		status_item = QTableWidgetItem()
		self.table.setItem(self.rowcount - 1, 3, status_item)

        # add column 4: kill button to kill the relative process
		killbtn = QPushButton(self.table)
		killbtn.setText('Kill')
		self.table.setCellWidget(self.rowcount - 1, 4, killbtn)
		
        # Initiate a QProcess running a system command
		process = QProcess()
		command = "python 01_Crering.py"#command = 'python3' + ' ' + os.getcwd() + '/' + " 01_CNN.py " + ' ' + Mainwindow.cmd
		process.setProcessChannelMode(QProcess.MergedChannels)
        # connect the stdout_item to the Process StandardOutput
        # it gets constantly update as the process emit std output
		process.readyReadStandardOutput.connect(lambda: stdout_item.setText(str(process.readAllStandardOutput().data().decode('utf-8'))))
        # start the process
		process.start(command)
        # this was supposed to add the process status in the relative column ... BUT it DOESN'T do it
		status_item.setText(str(process.ProcessState()))
        # connect the kill button to the process.kill method, to stop the process
		killbtn.clicked.connect(process.kill)
		killbtn.clicked.connect(lambda: killbtn.setText('Killed'))
        # this was supposed to 'UPDATE' the process status (from running to stoppted) in the relative column ... BUT it DOESN'T do it
		killbtn.clicked.connect(lambda: status_item.setText(str(process.ProcessState())))
        # append the process to a list so that it doesn't get destroyed at each run
		self.mylistofprocesses.append(process)
"""


if __name__ == "__main__":
	app = QApplication(sys.argv)
	Mainwindow = MainWindow()
	Mainwindow.show()
	#ex = runcommands()
	#ex.show()
	app.exec_()
