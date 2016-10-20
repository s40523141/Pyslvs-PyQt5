# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/info/options.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 485)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/shaded.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.option_tab = QtWidgets.QTabWidget(Dialog)
        self.option_tab.setObjectName("option_tab")
        self.general_tab = QtWidgets.QWidget()
        self.general_tab.setObjectName("general_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.general_tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.general_tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ZoomFactor = QtWidgets.QSpinBox(self.general_tab)
        self.ZoomFactor.setMinimum(1)
        self.ZoomFactor.setMaximum(10)
        self.ZoomFactor.setProperty("value", 2)
        self.ZoomFactor.setObjectName("ZoomFactor")
        self.gridLayout.addWidget(self.ZoomFactor, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.general_tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.EnvVariable = QtWidgets.QLineEdit(self.general_tab)
        self.EnvVariable.setObjectName("EnvVariable")
        self.gridLayout.addWidget(self.EnvVariable, 0, 1, 1, 1)
        self.TableToolLocation = QtWidgets.QComboBox(self.general_tab)
        self.TableToolLocation.setObjectName("TableToolLocation")
        self.TableToolLocation.addItem("")
        self.TableToolLocation.addItem("")
        self.gridLayout.addWidget(self.TableToolLocation, 2, 1, 1, 1)
        self.ViewBarLocation = QtWidgets.QComboBox(self.general_tab)
        self.ViewBarLocation.setObjectName("ViewBarLocation")
        self.ViewBarLocation.addItem("")
        self.ViewBarLocation.addItem("")
        self.gridLayout.addWidget(self.ViewBarLocation, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.general_tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.general_tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.general_tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.ToolPanelLocation = QtWidgets.QComboBox(self.general_tab)
        self.ToolPanelLocation.setObjectName("ToolPanelLocation")
        self.ToolPanelLocation.addItem("")
        self.ToolPanelLocation.addItem("")
        self.gridLayout.addWidget(self.ToolPanelLocation, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 220, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.option_tab.addTab(self.general_tab, "")
        self.appearance_tab = QtWidgets.QWidget()
        self.appearance_tab.setObjectName("appearance_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.appearance_tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.appearance_tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.appearance_tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.appearance_tab)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.appearance_tab)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_2.addWidget(self.comboBox_6, 2, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.appearance_tab)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_2.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.appearance_tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.appearance_tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.appearance_tab)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_2.addWidget(self.comboBox_7, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 256, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.option_tab.addTab(self.appearance_tab, "")
        self.verticalLayout.addWidget(self.option_tab)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Exit_button = QtWidgets.QDialogButtonBox(Dialog)
        self.Exit_button.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.Exit_button.setObjectName("Exit_button")
        self.horizontalLayout.addWidget(self.Exit_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.option_tab.setCurrentIndex(0)
        self.Exit_button.accepted.connect(Dialog.accept)
        self.Exit_button.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.label_2.setText(_translate("Dialog", "Zoom factor:"))
        self.label.setText(_translate("Dialog", "Environment variable:"))
        self.TableToolLocation.setItemText(0, _translate("Dialog", "Left"))
        self.TableToolLocation.setItemText(1, _translate("Dialog", "Right"))
        self.ViewBarLocation.setItemText(0, _translate("Dialog", "Buttom"))
        self.ViewBarLocation.setItemText(1, _translate("Dialog", "Top"))
        self.label_3.setText(_translate("Dialog", "Table Tool Location:"))
        self.label_4.setText(_translate("Dialog", "View Bar Location:"))
        self.label_5.setText(_translate("Dialog", "Tool Panel Location:"))
        self.ToolPanelLocation.setItemText(0, _translate("Dialog", "Buttom"))
        self.ToolPanelLocation.setItemText(1, _translate("Dialog", "Top"))
        self.option_tab.setTabText(self.option_tab.indexOf(self.general_tab), _translate("Dialog", "General"))
        self.label_7.setText(_translate("Dialog", "Stay Chain Color:"))
        self.label_6.setText(_translate("Dialog", "Link Rod Color:"))
        self.label_8.setText(_translate("Dialog", "Auxiliary Line Color:"))
        self.label_9.setText(_translate("Dialog", "Auxiliary Line Limit Color:"))
        self.option_tab.setTabText(self.option_tab.indexOf(self.appearance_tab), _translate("Dialog", "Appearance"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

