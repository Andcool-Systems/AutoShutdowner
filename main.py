from PyQt5 import QtWidgets, uic, QtGui
import os
from datetime import datetime  #Модуль времени
import sys
app = QtWidgets.QApplication([])
try:
    os.chdir(sys._MEIPASS)
    ui = uic.loadUi("program.ui")
    ui.setWindowIcon(QtGui.QIcon('power.ico'))
except:
    ui = uic.loadUi("program.ui")
    ui.setWindowIcon(QtGui.QIcon('power.ico'))
ui.setWindowTitle("Shutdown")
ui.setFixedSize(339, 213)
def start():
    tab = ui.tabWidget.currentIndex()
    if tab == 0:
        seconds = ui.sec1.value() + (ui.min1.value() * 60) + (ui.hou1.value() * 3600) + (ui.day1.value() * 86400)
        print(seconds)
        os.system(f"shutdown -s -t {seconds}")

    elif tab == 1:
        seconds = ui.sec2.value() + (ui.min2.value() * 60) + (ui.hou2.value() * 3600)
        now_time_log = datetime.now()
        seconds_now = int(now_time_log.second) + (int(now_time_log.minute) * 60) + (int(now_time_log.hour) * 3600)

        if seconds > seconds_now: os.system(f"shutdown -s -t {seconds - seconds_now}")
        else: 
            seconds += 86400
            os.system(f"shutdown -s -t {seconds - seconds_now}")


def stop(): os.system("shutdown -a")

ui.start.clicked.connect(start)
ui.stop.clicked.connect(stop)


now_time_log = datetime.now()

ui.min2.setValue(int(now_time_log.minute))
ui.hou2.setValue(int(now_time_log.hour))


ui.show()
app.exec()