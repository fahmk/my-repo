# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'muja.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 525)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/dis.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(13, 13, 13);\n"
"    ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}\n"
"")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 7, 0, 1, 1)
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 2, 1, 1, 1)
        self.push_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_del.setObjectName("push_del")
        self.gridLayout.addWidget(self.push_del, 1, 2, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 2, 2, 1, 1)
        self.push_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_minus.sizePolicy().hasHeightForWidth())
        self.push_minus.setSizePolicy(sizePolicy)
        self.push_minus.setStyleSheet("QPushButton{\n"
"font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(20, 255, 197);\n"
"   \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(28, 111, 35);\n"
" border -radius:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(77, 255, 74);\n"
"  \n"
"    background-color: rgb(19, 61, 8);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(9, 31, 2);\n"
"    color: rgb(106, 255, 42);\n"
"}\n"
"    ")
        self.push_minus.setObjectName("push_minus")
        self.gridLayout.addWidget(self.push_minus, 2, 3, 1, 1)
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 5, 1, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 7, 1, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 5, 2, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 5, 0, 1, 1)
        self.push_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        self.push_clear.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 1, 0, 1, 2)
        self.push_zero = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_zero.sizePolicy().hasHeightForWidth())
        self.push_zero.setSizePolicy(sizePolicy)
        self.push_zero.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_zero.setObjectName("push_zero")
        self.gridLayout.addWidget(self.push_zero, 8, 0, 1, 2)
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 7, 2, 1, 1)
        self.push_divide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_divide.sizePolicy().hasHeightForWidth())
        self.push_divide.setSizePolicy(sizePolicy)
        self.push_divide.setStyleSheet("QPushButton{\n"
"font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(20, 255, 197);\n"
"   \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(28, 111, 35);\n"
" border -radius:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(77, 255, 74);\n"
"  \n"
"    background-color: rgb(19, 61, 8);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(9, 31, 2);\n"
"    color: rgb(106, 255, 42);\n"
"}\n"
"    ")
        self.push_divide.setObjectName("push_divide")
        self.gridLayout.addWidget(self.push_divide, 5, 3, 1, 1)
        self.push_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_equal.sizePolicy().hasHeightForWidth())
        self.push_equal.setSizePolicy(sizePolicy)
        self.push_equal.setStyleSheet("QPushButton{\n"
"font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(20, 255, 197);\n"
"   \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(28, 111, 35);\n"
" border -radius:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(77, 255, 74);\n"
"  \n"
"    background-color: rgb(19, 61, 8);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(9, 31, 2);\n"
"    color: rgb(106, 255, 42);\n"
"}\n"
"    ")
        self.push_equal.setObjectName("push_equal")
        self.gridLayout.addWidget(self.push_equal, 8, 3, 1, 1)
        self.push_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_point.sizePolicy().hasHeightForWidth())
        self.push_point.setSizePolicy(sizePolicy)
        self.push_point.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_point.setObjectName("push_point")
        self.gridLayout.addWidget(self.push_point, 8, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.push_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_plus.sizePolicy().hasHeightForWidth())
        self.push_plus.setSizePolicy(sizePolicy)
        self.push_plus.setStyleSheet("QPushButton{\n"
"font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(20, 255, 197);\n"
"   \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(28, 111, 35);\n"
" border -radius:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(77, 255, 74);\n"
"  \n"
"    background-color: rgb(19, 61, 8);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(9, 31, 2);\n"
"    color: rgb(106, 255, 42);\n"
"}\n"
"    ")
        self.push_plus.setObjectName("push_plus")
        self.gridLayout.addWidget(self.push_plus, 1, 3, 1, 1)
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton{\n"
"font: 26pt \"MS Serif\";\n"
"    \n"
"    color: rgb(46, 10, 255);\n"
"    \n"
"    background-color: rgb(189, 189, 189);\n"
" border -radius:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
";\n"
"    \n"
"    color: rgb(0, 5, 81);\n"
"  \n"
"    \n"
"    background-color: rgb(59, 59, 63);\n"
"}\n"
"\n"
"\n"
"    QPushButton{\n"
"       \n"
"    \n"
"    background-color: rgb(106, 110, 115);\n"
"  \n"
"    color: rgb(29, 0, 255);\n"
"}")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 2, 0, 1, 1)
        self.push_multiply = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.push_multiply.sizePolicy().hasHeightForWidth())
        self.push_multiply.setSizePolicy(sizePolicy)
        self.push_multiply.setStyleSheet("QPushButton{\n"
"font: 75 36pt \"MS Shell Dlg 2\";\n"
"    \n"
"    color: rgb(20, 255, 197);\n"
"   \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(28, 111, 35);\n"
" border -radius:28px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(77, 255, 74);\n"
"  \n"
"    background-color: rgb(19, 61, 8);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(9, 31, 2);\n"
"    color: rgb(106, 255, 42);\n"
"}\n"
"    ")
        self.push_multiply.setObjectName("push_multiply")
        self.gridLayout.addWidget(self.push_multiply, 7, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        
        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connect(self.method_2)
        self.push_3.clicked.connect(self.method_3)
        self.push_4.clicked.connect(self.method_4)
        self.push_5.clicked.connect(self.method_5)
        self.push_6.clicked.connect(self.method_6)
        self.push_7.clicked.connect(self.method_7)
        self.push_8.clicked.connect(self.method_8)
        self.push_9.clicked.connect(self.method_9)
        self.push_zero.clicked.connect(self.method_zero)
        self.push_point.clicked.connect(self.method_point)
        self.push_plus.clicked.connect(self.method_plus)
        self.push_minus.clicked.connect(self.method_minus)
        self.push_divide.clicked.connect(self.method_divide)
        self.push_multiply.clicked.connect(self.method_multiply)
        self.push_equal.clicked.connect(self.method_equal)
        self.push_clear.clicked.connect(self.method_clear)
        self.push_del.clicked.connect(self.method_del)


    def method_1(self):
        text=self.label.text()
        self.label.setText(text+"1")

    def method_2(self):
        text=self.label.text()
        self.label.setText(text+"2")

    def method_3(self):
        text=self.label.text()
        self.label.setText(text+"3")

    def method_4(self):
        text=self.label.text()
        self.label.setText(text+"4")

    def method_5(self):
        text=self.label.text()
        self.label.setText(text+"5")

    def method_6(self):
        text=self.label.text()
        self.label.setText(text+"6")

    def method_7(self):
        text=self.label.text()
        self.label.setText(text+"7")

    def method_8(self):
        text=self.label.text()
        self.label.setText(text+"8")

    def method_9(self):
        text=self.label.text()
        self.label.setText(text+"9")
        
    def method_zero(self):
        text=self.label.text()
        self.label.setText(text+"0")

    def method_point(self):
        text=self.label.text()
        self.label.setText(text+".")

    def method_plus(self):
        text=self.label.text()
        self.label.setText(text+"+")

    def method_minus(self):
        text=self.label.text()
        self.label.setText(text+"-")

    def method_multiply(self):
        text=self.label.text()
        self.label.setText(text+"*")

    def method_divide(self):
        text=self.label.text()
        self.label.setText(text+"/")

    def method_clear(self):
        self.label.setText("")
        

    def method_del(self):
        text=self.label.text()
        self.label.setText(text[:len(text)-1])

    def method_equal(self):
        text=self.label.text()

        try:
            ans=eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("wrong input")


   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.push_7.setText(_translate("MainWindow", "7"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_del.setText(_translate("MainWindow", "Del"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_minus.setText(_translate("MainWindow", "_"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_8.setText(_translate("MainWindow", "8"))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_clear.setText(_translate("MainWindow", "Clear"))
        self.push_zero.setText(_translate("MainWindow", "0"))
        self.push_9.setText(_translate("MainWindow", "9"))
        self.push_divide.setText(_translate("MainWindow", "/"))
        self.push_equal.setText(_translate("MainWindow", "="))
        self.push_point.setText(_translate("MainWindow", "."))
        self.label.setText(_translate("MainWindow", "0"))
        self.push_plus.setText(_translate("MainWindow", "+"))
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_multiply.setText(_translate("MainWindow", "*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
