# -*- coding: utf-8 -*-
from .modules import *

class edit_shaft_show(QDialog, edit_shaft_Dialog):
    Another_shaft = pyqtSignal(int)
    def __init__(self, table1, table2, pos, parent=None):
        super(edit_shaft_show, self).__init__(parent)
        self.setupUi(self)
        icon = QIcon(QPixmap(":/icons/point.png"))
        for i in range(table1.rowCount()):
            self.Shaft_Center.insertItem(i, icon, table1.item(i, 0).text())
            self.References.insertItem(i, icon, table1.item(i, 0).text())
        for i in range(table2.rowCount()): self.Shaft.insertItem(i, QIcon(QPixmap(":/icons/circle.png")), table2.item(i, 0).text())
        self.Shaft.setCurrentIndex(pos)
    
    @pyqtSlot(int)
    def on_Shaft_currentIndexChanged(self, index): self.Another_shaft.emit(index)
    
    @pyqtSlot(int, int, float, float)
    def change_feedback(self, center, references, start, end):
        self.Shaft_Center.setCurrentIndex(center)
        self.References.setCurrentIndex(references)
        self.Start_Angle.setValue(start)
        self.End_Angle.setValue(end)
    
    @pyqtSlot(float)
    def on_Start_Angle_valueChanged(self, p0): self.isOk()
    @pyqtSlot(float)
    def on_End_Angle_valueChanged(self, p0): self.isOk()
    @pyqtSlot()
    def on_Start_Angle_editingFinished(self): self.isOk()
    @pyqtSlot()
    def on_End_Angle_editingFinished(self): self.isOk()
    @pyqtSlot(int)
    def on_Shaft_Center_currentIndexChanged(self, index): self.isOk()
    @pyqtSlot(int)
    def on_References_currentIndexChanged(self, index): self.isOk()
    def isOk(self):
        self.center = self.Shaft_Center.currentText()
        self.ref = self.References.currentText()
        self.start = self.Start_Angle.text()
        self.end = self.End_Angle.text()
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(self.center!=self.ref and self.start!=self.end)
