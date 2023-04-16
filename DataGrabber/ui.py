# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './DataGrabber.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 794)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
"}\n"
"\n"
"QCheckBox{\n"
"font-family:Arial;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"}\n"
"QRadioButton{\n"
"font-family:Arial;\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"}\n"
"QLabel{\n"
"font-family:Arial;\n"
"color:#222\n"
"}\n"
"\n"
"#pushButton_load,#pushButton_picker,#pushButton_start,#pushButton_eraser,#pushButton_reset,#pushButton_add\n"
"{\n"
"background:    white;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"border-radius:5px;\n"
"font-family:Arial;\n"
"}\n"
"#pushButton_load:hover,#pushButton_picker:hover,#pushButton_start:hover,#pushButton_reset:hover,#pushButton_add:hover,#pushButton_eraser:hover{\n"
"background:    orange;\n"
"}\n"
"QLineEdit{\n"
"border-radius:4px;\n"
"background:white;\n"
"}\n"
"#label_info{\n"
"color:white;\n"
"background:#ef5350;\n"
"padding:10px\n"
"}\n"
"#label_img{\n"
"cursor:crosshair;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setMinimumSize(QtCore.QSize(0, 400))
        self.label_img.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_img.setObjectName("label_img")
        self.gridLayout.addWidget(self.label_img, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftbottom = QtWidgets.QPushButton(self.centralwidget)
        self.leftbottom.setMinimumSize(QtCore.QSize(0, 40))
        self.leftbottom.setObjectName("leftbottom")
        self.horizontalLayout_2.addWidget(self.leftbottom)
        self.righttop = QtWidgets.QPushButton(self.centralwidget)
        self.righttop.setMinimumSize(QtCore.QSize(0, 40))
        self.righttop.setObjectName("righttop")
        self.horizontalLayout_2.addWidget(self.righttop)
        self.auto_axis = QtWidgets.QPushButton(self.centralwidget)
        self.auto_axis.setMinimumSize(QtCore.QSize(0, 40))
        self.auto_axis.setObjectName("auto_axis")
        self.horizontalLayout_2.addWidget(self.auto_axis)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(40, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.lineEdit_xmin = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_xmin.sizePolicy().hasHeightForWidth())
        self.lineEdit_xmin.setSizePolicy(sizePolicy)
        self.lineEdit_xmin.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_xmin.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_xmin.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_xmin.setFont(font)
        self.lineEdit_xmin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_xmin.setObjectName("lineEdit_xmin")
        self.horizontalLayout_12.addWidget(self.lineEdit_xmin)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.lineEdit_xmax = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_xmax.sizePolicy().hasHeightForWidth())
        self.lineEdit_xmax.setSizePolicy(sizePolicy)
        self.lineEdit_xmax.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_xmax.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_xmax.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_xmax.setFont(font)
        self.lineEdit_xmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_xmax.setObjectName("lineEdit_xmax")
        self.horizontalLayout_12.addWidget(self.lineEdit_xmax)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.checkBox_logx = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_logx.sizePolicy().hasHeightForWidth())
        self.checkBox_logx.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_logx.setFont(font)
        self.checkBox_logx.setObjectName("checkBox_logx")
        self.horizontalLayout_12.addWidget(self.checkBox_logx)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(40, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_ymin = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ymin.sizePolicy().hasHeightForWidth())
        self.lineEdit_ymin.setSizePolicy(sizePolicy)
        self.lineEdit_ymin.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_ymin.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_ymin.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_ymin.setFont(font)
        self.lineEdit_ymin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ymin.setObjectName("lineEdit_ymin")
        self.horizontalLayout_5.addWidget(self.lineEdit_ymin)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_ymax = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ymax.sizePolicy().hasHeightForWidth())
        self.lineEdit_ymax.setSizePolicy(sizePolicy)
        self.lineEdit_ymax.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_ymax.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_ymax.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_ymax.setFont(font)
        self.lineEdit_ymax.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ymax.setObjectName("lineEdit_ymax")
        self.horizontalLayout_5.addWidget(self.lineEdit_ymax)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.checkBox_logy = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.checkBox_logy.sizePolicy().hasHeightForWidth())
        self.checkBox_logy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_logy.setFont(font)
        self.checkBox_logy.setObjectName("checkBox_logy")
        self.horizontalLayout_5.addWidget(self.checkBox_logy)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSlider_eraser = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_eraser.setMinimum(1)
        self.horizontalSlider_eraser.setMaximum(100)
        self.horizontalSlider_eraser.setProperty("value", 20)
        self.horizontalSlider_eraser.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_eraser.setInvertedAppearance(False)
        self.horizontalSlider_eraser.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_eraser.setObjectName("horizontalSlider_eraser")
        self.gridLayout_2.addWidget(self.horizontalSlider_eraser, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalSlider_spacing = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_spacing.setWhatsThis("")
        self.horizontalSlider_spacing.setMinimum(1)
        self.horizontalSlider_spacing.setMaximum(100)
        self.horizontalSlider_spacing.setSingleStep(1)
        self.horizontalSlider_spacing.setProperty("value", 1)
        self.horizontalSlider_spacing.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_spacing.setObjectName("horizontalSlider_spacing")
        self.gridLayout_2.addWidget(self.horizontalSlider_spacing, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.horizontalSlider_morph = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_morph.setMinimum(1)
        self.horizontalSlider_morph.setMaximum(1000)
        self.horizontalSlider_morph.setProperty("value", 20)
        self.horizontalSlider_morph.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_morph.setObjectName("horizontalSlider_morph")
        self.gridLayout_2.addWidget(self.horizontalSlider_morph, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(40, 0))
        self.label_8.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(40, 0))
        self.label_9.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(40, 0))
        self.label_10.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.color_preview = QtWidgets.QPushButton(self.centralwidget)
        self.color_preview.setMinimumSize(QtCore.QSize(30, 30))
        self.color_preview.setMaximumSize(QtCore.QSize(30, 30))
        self.color_preview.setStyleSheet("QPushButton{background-color: grey};")
        self.color_preview.setText("")
        self.color_preview.setObjectName("color_preview")
        self.horizontalLayout_10.addWidget(self.color_preview)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_load.sizePolicy().hasHeightForWidth())
        self.pushButton_load.setSizePolicy(sizePolicy)
        self.pushButton_load.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_load.setFont(font)
        self.pushButton_load.setStyleSheet("icon:url(:/grabber/load.png)")
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout_10.addWidget(self.pushButton_load)
        self.pushButton_picker = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_picker.sizePolicy().hasHeightForWidth())
        self.pushButton_picker.setSizePolicy(sizePolicy)
        self.pushButton_picker.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_picker.setFont(font)
        self.pushButton_picker.setStyleSheet("icon:url(:/grabber/color-picker.png)")
        self.pushButton_picker.setObjectName("pushButton_picker")
        self.horizontalLayout_10.addWidget(self.pushButton_picker)
        self.pushButton_eraser = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_eraser.sizePolicy().hasHeightForWidth())
        self.pushButton_eraser.setSizePolicy(sizePolicy)
        self.pushButton_eraser.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_eraser.setFont(font)
        self.pushButton_eraser.setStyleSheet("icon:url(:/grabber/eraser_2.png)")
        self.pushButton_eraser.setObjectName("pushButton_eraser")
        self.horizontalLayout_10.addWidget(self.pushButton_eraser)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("icon:url(:/grabber/下载.png)")
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_10.addWidget(self.pushButton_add)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("icon:url(:/grabber/3596215.png)")
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_10.addWidget(self.pushButton_start)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setObjectName("menubar")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuExport_to_TXT = QtWidgets.QMenu(self.menufile)
        self.menuExport_to_TXT.setObjectName("menuExport_to_TXT")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport_to_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_to_CSV.setObjectName("actionExport_to_CSV")
        self.actionExport_to_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Excel.setObjectName("actionExport_to_Excel")
        self.actionTXT = QtWidgets.QAction(MainWindow)
        self.actionTXT.setObjectName("actionTXT")
        self.actionExcel = QtWidgets.QAction(MainWindow)
        self.actionExcel.setObjectName("actionExcel")
        self.actionCSV = QtWidgets.QAction(MainWindow)
        self.actionCSV.setObjectName("actionCSV")
        self.menuhelp.addAction(self.actionAbout)
        self.menuExport_to_TXT.addAction(self.actionTXT)
        self.menuExport_to_TXT.addAction(self.actionCSV)
        self.menufile.addAction(self.actionImport)
        self.menufile.addAction(self.menuExport_to_TXT.menuAction())
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSlider_spacing.sliderReleased.connect(MainWindow.set_spacing)
        self.horizontalSlider_spacing.valueChanged['int'].connect(self.label_10.setNum)
        self.horizontalSlider_morph.valueChanged['int'].connect(self.label_9.setNum)
        self.horizontalSlider_eraser.valueChanged['int'].connect(self.label_8.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataGrabber"))
        self.label_info.setText(_translate("MainWindow", "STEP1: Load Graph"))
        self.label_img.setText(_translate("MainWindow", "Label_img"))
        self.leftbottom.setText(_translate("MainWindow", "left bottom"))
        self.righttop.setText(_translate("MainWindow", "right top"))
        self.auto_axis.setText(_translate("MainWindow", "Auto"))
        self.label_3.setText(_translate("MainWindow", "xmin"))
        self.lineEdit_xmin.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "xmax"))
        self.lineEdit_xmax.setText(_translate("MainWindow", "1"))
        self.checkBox_logx.setText(_translate("MainWindow", "Logx"))
        self.label_6.setText(_translate("MainWindow", "ymin"))
        self.lineEdit_ymin.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "ymax"))
        self.lineEdit_ymax.setText(_translate("MainWindow", "1"))
        self.checkBox_logy.setText(_translate("MainWindow", "Logy"))
        self.label.setText(_translate("MainWindow", "Eraser size"))
        self.horizontalSlider_spacing.setToolTip(_translate("MainWindow", "Adjust the steps(by pixel) to extract data "))
        self.label_7.setText(_translate("MainWindow", "Spacing"))
        self.label_5.setText(_translate("MainWindow", "Morph size"))
        self.label_8.setText(_translate("MainWindow", "20"))
        self.label_9.setText(_translate("MainWindow", "20"))
        self.label_10.setText(_translate("MainWindow", "1"))
        self.pushButton_load.setText(_translate("MainWindow", "load"))
        self.pushButton_picker.setText(_translate("MainWindow", "picker"))
        self.pushButton_eraser.setText(_translate("MainWindow", "eraser"))
        self.pushButton_add.setText(_translate("MainWindow", "add"))
        self.pushButton_start.setText(_translate("MainWindow", "preview"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuExport_to_TXT.setTitle(_translate("MainWindow", "Export"))
        self.actionAbout.setText(_translate("MainWindow", "V1.0"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport_to_CSV.setText(_translate("MainWindow", "Export to CSV"))
        self.actionExport_to_Excel.setText(_translate("MainWindow", "Export to Excel"))
        self.actionTXT.setText(_translate("MainWindow", "TXT"))
        self.actionExcel.setText(_translate("MainWindow", "Excel"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))
import Datagrabber_rc
