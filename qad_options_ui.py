# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qad_options.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Options_Dialog(object):
    def setupUi(self, Options_Dialog):
        Options_Dialog.setObjectName("Options_Dialog")
        Options_Dialog.setWindowModality(QtCore.Qt.NonModal)
        Options_Dialog.resize(591, 386)
        Options_Dialog.setMinimumSize(QtCore.QSize(591, 386))
        Options_Dialog.setMaximumSize(QtCore.QSize(591, 386))
        Options_Dialog.setSizeGripEnabled(False)
        Options_Dialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Options_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Options_Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 571, 331))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.DisplayTab = QtWidgets.QWidget()
        self.DisplayTab.setObjectName("DisplayTab")
        self.groupBox = QtWidgets.QGroupBox(self.DisplayTab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 251, 291))
        self.groupBox.setObjectName("groupBox")
        self.Button_TextWindowColor = QtWidgets.QPushButton(self.groupBox)
        self.Button_TextWindowColor.setGeometry(QtCore.QRect(20, 260, 91, 23))
        self.Button_TextWindowColor.setObjectName("Button_TextWindowColor")
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setGeometry(QtCore.QRect(20, 100, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setObjectName("checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE")
        self.checkBox_SHOWTEXTWINDOW = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_SHOWTEXTWINDOW.setGeometry(QtCore.QRect(10, 20, 231, 20))
        self.checkBox_SHOWTEXTWINDOW.setObjectName("checkBox_SHOWTEXTWINDOW")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 191, 21))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit_CMDINPUTHISTORYMAX = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_CMDINPUTHISTORYMAX.setGeometry(QtCore.QRect(10, 50, 31, 20))
        self.lineEdit_CMDINPUTHISTORYMAX.setObjectName("lineEdit_CMDINPUTHISTORYMAX")
        self.lineEdit_INPUTSEARCHDELAY = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_INPUTSEARCHDELAY.setGeometry(QtCore.QRect(20, 180, 41, 20))
        self.lineEdit_INPUTSEARCHDELAY.setObjectName("lineEdit_INPUTSEARCHDELAY")
        self.label_INPUTSEARCHDELAY = QtWidgets.QLabel(self.groupBox)
        self.label_INPUTSEARCHDELAY.setGeometry(QtCore.QRect(70, 180, 171, 21))
        self.label_INPUTSEARCHDELAY.setWordWrap(True)
        self.label_INPUTSEARCHDELAY.setObjectName("label_INPUTSEARCHDELAY")
        self.checkBox_INPUTSEARCHOPTIONS_ON = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_ON.setGeometry(QtCore.QRect(10, 80, 231, 17))
        self.checkBox_INPUTSEARCHOPTIONS_ON.setObjectName("checkBox_INPUTSEARCHOPTIONS_ON")
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setGeometry(QtCore.QRect(20, 120, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setObjectName("checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST")
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setGeometry(QtCore.QRect(20, 140, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setObjectName("checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON")
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setGeometry(QtCore.QRect(20, 160, 211, 17))
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setObjectName("checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR")
        self.groupBox_2 = QtWidgets.QGroupBox(self.DisplayTab)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 10, 281, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_ARCMINSEGMENTQTY = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_ARCMINSEGMENTQTY.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_ARCMINSEGMENTQTY.setObjectName("lineEdit_ARCMINSEGMENTQTY")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 30, 221, 21))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 221, 21))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit_CIRCLEMINSEGMENTQTY = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_CIRCLEMINSEGMENTQTY.setGeometry(QtCore.QRect(10, 60, 31, 20))
        self.lineEdit_CIRCLEMINSEGMENTQTY.setObjectName("lineEdit_CIRCLEMINSEGMENTQTY")
        self.lineEdit_TOLERANCE2APPROXCURVE = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_TOLERANCE2APPROXCURVE.setGeometry(QtCore.QRect(10, 90, 31, 20))
        self.lineEdit_TOLERANCE2APPROXCURVE.setObjectName("lineEdit_TOLERANCE2APPROXCURVE")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 221, 41))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.DisplayTab)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 140, 281, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_CURSORSIZE = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_CURSORSIZE.setGeometry(QtCore.QRect(10, 20, 31, 20))
        self.lineEdit_CURSORSIZE.setObjectName("lineEdit_CURSORSIZE")
        self.horizontalSlider_CURSORSIZE = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_CURSORSIZE.setGeometry(QtCore.QRect(50, 20, 221, 22))
        self.horizontalSlider_CURSORSIZE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_CURSORSIZE.setObjectName("horizontalSlider_CURSORSIZE")
        self.tabWidget.addTab(self.DisplayTab, "")
        self.DraftingTab = QtWidgets.QWidget()
        self.DraftingTab.setObjectName("DraftingTab")
        self.groupBox_4 = QtWidgets.QGroupBox(self.DraftingTab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 261, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox_AUTOSNAP_DISPLAY_MARK = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setGeometry(QtCore.QRect(10, 20, 241, 17))
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setObjectName("checkBox_AUTOSNAP_DISPLAY_MARK")
        self.pushButton_AutoSnapColor = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_AutoSnapColor.setGeometry(QtCore.QRect(10, 110, 81, 23))
        self.pushButton_AutoSnapColor.setObjectName("pushButton_AutoSnapColor")
        self.checkBox_APBOX = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_APBOX.setGeometry(QtCore.QRect(10, 80, 241, 17))
        self.checkBox_APBOX.setObjectName("checkBox_APBOX")
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setGeometry(QtCore.QRect(10, 60, 241, 17))
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setObjectName("checkBox_AUTOSNAP_DISPLAY_TOOLTIPS")
        self.checkBox_AUTOSNAP_MAGNET = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_AUTOSNAP_MAGNET.setGeometry(QtCore.QRect(10, 40, 241, 17))
        self.checkBox_AUTOSNAP_MAGNET.setObjectName("checkBox_AUTOSNAP_MAGNET")
        self.groupBox_5 = QtWidgets.QGroupBox(self.DraftingTab)
        self.groupBox_5.setGeometry(QtCore.QRect(290, 10, 261, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_POLARMODE_AUTO_ACQUIRE = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setGeometry(QtCore.QRect(10, 20, 241, 17))
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setObjectName("radioButton_POLARMODE_AUTO_ACQUIRE")
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setGeometry(QtCore.QRect(10, 40, 241, 17))
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setObjectName("radioButton_POLARMODE_SHIFT_TO_ACQUIRE")
        self.groupBox_6 = QtWidgets.QGroupBox(self.DraftingTab)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 160, 261, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalSlider_AUTOSNAPSIZE = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider_AUTOSNAPSIZE.setGeometry(QtCore.QRect(70, 30, 181, 22))
        self.horizontalSlider_AUTOSNAPSIZE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_AUTOSNAPSIZE.setObjectName("horizontalSlider_AUTOSNAPSIZE")
        self.widget_AUTOSNAPSIZE = QtWidgets.QWidget(self.groupBox_6)
        self.widget_AUTOSNAPSIZE.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_AUTOSNAPSIZE.setObjectName("widget_AUTOSNAPSIZE")
        self.groupBox_7 = QtWidgets.QGroupBox(self.DraftingTab)
        self.groupBox_7.setGeometry(QtCore.QRect(290, 160, 261, 81))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalSlider_APERTURE = QtWidgets.QSlider(self.groupBox_7)
        self.horizontalSlider_APERTURE.setGeometry(QtCore.QRect(70, 30, 181, 22))
        self.horizontalSlider_APERTURE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_APERTURE.setObjectName("horizontalSlider_APERTURE")
        self.widget_APERTURESIZE = QtWidgets.QWidget(self.groupBox_7)
        self.widget_APERTURESIZE.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_APERTURESIZE.setObjectName("widget_APERTURESIZE")
        self.tabWidget.addTab(self.DraftingTab, "")
        self.SelectionTab = QtWidgets.QWidget()
        self.SelectionTab.setObjectName("SelectionTab")
        self.groupBox_8 = QtWidgets.QGroupBox(self.SelectionTab)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 261, 81))
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalSlider_PICKBOX = QtWidgets.QSlider(self.groupBox_8)
        self.horizontalSlider_PICKBOX.setGeometry(QtCore.QRect(70, 30, 181, 22))
        self.horizontalSlider_PICKBOX.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_PICKBOX.setObjectName("horizontalSlider_PICKBOX")
        self.widget_PICKBOX = QtWidgets.QWidget(self.groupBox_8)
        self.widget_PICKBOX.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_PICKBOX.setObjectName("widget_PICKBOX")
        self.groupBox_9 = QtWidgets.QGroupBox(self.SelectionTab)
        self.groupBox_9.setGeometry(QtCore.QRect(280, 10, 271, 81))
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalSlider_GRIPSIZE = QtWidgets.QSlider(self.groupBox_9)
        self.horizontalSlider_GRIPSIZE.setGeometry(QtCore.QRect(70, 30, 191, 22))
        self.horizontalSlider_GRIPSIZE.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_GRIPSIZE.setObjectName("horizontalSlider_GRIPSIZE")
        self.widget_GRIPSIZE = QtWidgets.QWidget(self.groupBox_9)
        self.widget_GRIPSIZE.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.widget_GRIPSIZE.setObjectName("widget_GRIPSIZE")
        self.groupBox_10 = QtWidgets.QGroupBox(self.SelectionTab)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 100, 261, 131))
        self.groupBox_10.setObjectName("groupBox_10")
        self.checkBox_PICKFIRST = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_PICKFIRST.setGeometry(QtCore.QRect(10, 20, 241, 17))
        self.checkBox_PICKFIRST.setObjectName("checkBox_PICKFIRST")
        self.checkBox_PICKADD = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_PICKADD.setGeometry(QtCore.QRect(10, 40, 241, 17))
        self.checkBox_PICKADD.setObjectName("checkBox_PICKADD")
        self.groupBox_11 = QtWidgets.QGroupBox(self.SelectionTab)
        self.groupBox_11.setGeometry(QtCore.QRect(280, 100, 271, 131))
        self.groupBox_11.setObjectName("groupBox_11")
        self.button_GripColor = QtWidgets.QPushButton(self.groupBox_11)
        self.button_GripColor.setGeometry(QtCore.QRect(70, 20, 141, 23))
        self.button_GripColor.setObjectName("button_GripColor")
        self.checkBox_GRIPS = QtWidgets.QCheckBox(self.groupBox_11)
        self.checkBox_GRIPS.setGeometry(QtCore.QRect(10, 50, 251, 17))
        self.checkBox_GRIPS.setObjectName("checkBox_GRIPS")
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT = QtWidgets.QCheckBox(self.groupBox_11)
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setGeometry(QtCore.QRect(20, 70, 241, 17))
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setObjectName("checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT")
        self.lineEdit_GRIPOBJLIMIT = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_GRIPOBJLIMIT.setGeometry(QtCore.QRect(20, 100, 31, 20))
        self.lineEdit_GRIPOBJLIMIT.setObjectName("lineEdit_GRIPOBJLIMIT")
        self.label_GRIPOBJLIMIT = QtWidgets.QLabel(self.groupBox_11)
        self.label_GRIPOBJLIMIT.setGeometry(QtCore.QRect(60, 100, 201, 31))
        self.label_GRIPOBJLIMIT.setToolTip("")
        self.label_GRIPOBJLIMIT.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_GRIPOBJLIMIT.setWordWrap(True)
        self.label_GRIPOBJLIMIT.setObjectName("label_GRIPOBJLIMIT")
        self.tabWidget.addTab(self.SelectionTab, "")

        self.retranslateUi(Options_Dialog)
        self.tabWidget.setCurrentIndex(2)
        self.buttonBox.accepted.connect(Options_Dialog.ButtonBOX_Accepted)
        self.buttonBox.clicked['QAbstractButton*'].connect(Options_Dialog.ButtonBOX_Apply)
        self.buttonBox.helpRequested.connect(Options_Dialog.ButtonHELP_Pressed)
        self.checkBox_INPUTSEARCHOPTIONS_ON.clicked.connect(Options_Dialog.checkBox_INPUTSEARCHOPTIONS_ON_clicked)
        self.horizontalSlider_CURSORSIZE.sliderMoved['int'].connect(Options_Dialog.horizontalSlider_CURSORSIZE_moved)
        self.lineEdit_CURSORSIZE.textEdited['QString'].connect(Options_Dialog.lineEdit_CURSORSIZE_textChanged)
        self.horizontalSlider_CURSORSIZE.valueChanged['int'].connect(Options_Dialog.horizontalSlider_CURSORSIZE_moved)
        self.horizontalSlider_AUTOSNAPSIZE.valueChanged['int'].connect(Options_Dialog.horizontalSlider_AUTOSNAPSIZE_changed)
        self.horizontalSlider_APERTURE.valueChanged['int'].connect(Options_Dialog.horizontalSlider_APERTURE_changed)
        self.horizontalSlider_PICKBOX.valueChanged['int'].connect(Options_Dialog.horizontalSlider_PICKBOX_changed)
        self.horizontalSlider_GRIPSIZE.valueChanged['int'].connect(Options_Dialog.horizontalSlider_GRIPSIZE_changed)
        self.checkBox_GRIPS.clicked.connect(Options_Dialog.checkBox_GRIPS_ON_clicked)
        self.button_GripColor.clicked.connect(Options_Dialog.button_GripColor_clicked)
        self.Button_TextWindowColor.clicked.connect(Options_Dialog.Button_TextWindowColor_clicked)
        self.pushButton_AutoSnapColor.clicked.connect(Options_Dialog.Button_AutoSnapWindowColor_clicked)
        QtCore.QMetaObject.connectSlotsByName(Options_Dialog)

    def retranslateUi(self, Options_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Options_Dialog.setWindowTitle(_translate("Options_Dialog", "QAD - Options"))
        self.groupBox.setTitle(_translate("Options_Dialog", "Window Elements"))
        self.Button_TextWindowColor.setToolTip(_translate("Options_Dialog", "Displays the Drawing Window Colors dialog box."))
        self.Button_TextWindowColor.setText(_translate("Options_Dialog", "Colors"))
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setToolTip(_translate("Options_Dialog", "Automatically appends suggestions as each keystroke is entered after the second\n"
"                                keystroke (system variable INPUTSEARCHOPTIONS).\n"
"                            "))
        self.checkBox_INPUTSEARCHOPTIONS_AUTOCOMPLETE.setText(_translate("Options_Dialog", "AutoComplete"))
        self.checkBox_SHOWTEXTWINDOW.setToolTip(_translate("Options_Dialog", "Show the text window at startup (system variable SHOWTEXTWINDOW)."))
        self.checkBox_SHOWTEXTWINDOW.setText(_translate("Options_Dialog", "Show the text window at startup"))
        self.label_4.setText(_translate("Options_Dialog", "Maximun command history length"))
        self.lineEdit_CMDINPUTHISTORYMAX.setToolTip(_translate("Options_Dialog", "Sets the maximum number of previous input values that are stored for a prompt in a\n"
"                                command (system variable CMDINPUTHISTORYMAX).\n"
"                            "))
        self.lineEdit_INPUTSEARCHDELAY.setToolTip(_translate("Options_Dialog", "<html><head/><body><p>Controls the amount of time that\n"
"                                elapses before automated keyboard features display at the Command prompt.</p><p>Valid\n"
"                                values are real numbers from 100 to 10,000, which represent milliseconds.</p></body></html>\n"
"                            "))
        self.label_INPUTSEARCHDELAY.setText(_translate("Options_Dialog", "Delay time (msec)"))
        self.checkBox_INPUTSEARCHOPTIONS_ON.setToolTip(_translate("Options_Dialog", "Turns on/off all automated keyboard features when typing at the Command prompt\n"
"                                (system variable INPUTSEARCHOPTIONS).\n"
"                            "))
        self.checkBox_INPUTSEARCHOPTIONS_ON.setText(_translate("Options_Dialog", "Automated keyboard features"))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setToolTip(_translate("Options_Dialog", "Displays a list of suggestions as keystrokes are entered (system variable\n"
"                                INPUTSEARCHOPTIONS).\n"
"                            "))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_LIST.setText(_translate("Options_Dialog", "Displays a list of suggestions"))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setToolTip(_translate("Options_Dialog", "Displays the icon of the command or system variable, if available (system variable\n"
"                                INPUTSEARCHOPTIONS).\n"
"                            "))
        self.checkBox_INPUTSEARCHOPTIONS_DISPLAY_ICON.setText(_translate("Options_Dialog", "Displays the icon of the command"))
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setToolTip(_translate("Options_Dialog", "Excludes the display of system variables (system variable INPUTSEARCHOPTIONS).\n"
"                            "))
        self.checkBox_INPUTSEARCHOPTIONS_EXCLUDE_SYS_VAR.setText(_translate("Options_Dialog", "Excludes system variables"))
        self.groupBox_2.setTitle(_translate("Options_Dialog", "Resolution"))
        self.lineEdit_ARCMINSEGMENTQTY.setToolTip(_translate("Options_Dialog", "Minimum number of segments to approximate an arc (system variable\n"
"                                ARCMINSEGMENTQTY).\n"
"                            "))
        self.label.setText(_translate("Options_Dialog", "Minimum number of segments in an arc"))
        self.label_2.setToolTip(_translate("Options_Dialog", "Minimum number of segments to approximate a circle (system variable\n"
"                                CIRCLEMINSEGMENTQTY).\n"
"                            "))
        self.label_2.setText(_translate("Options_Dialog", "Minimum number of segments in a circle"))
        self.lineEdit_CIRCLEMINSEGMENTQTY.setToolTip(_translate("Options_Dialog", "Minimum number of segments to approximate a circle (system variable\n"
"                                CIRCLEMINSEGMENTQTY).\n"
"                            "))
        self.lineEdit_TOLERANCE2APPROXCURVE.setToolTip(_translate("Options_Dialog", "Maximum error approximating a curve to segments (system variable\n"
"                                TOLERANCE2APPROXCURVE).\n"
"                            "))
        self.label_3.setText(_translate("Options_Dialog", "Maximun admitted error between a real curve and the aproximated, segmented curve\n"
"                            "))
        self.groupBox_3.setTitle(_translate("Options_Dialog", "Crosshair size"))
        self.lineEdit_CURSORSIZE.setToolTip(_translate("Options_Dialog", "Determines the size of the crosshair as a percentage of the screen size (system\n"
"                                variable CURSORSIZE).\n"
"                            "))
        self.horizontalSlider_CURSORSIZE.setToolTip(_translate("Options_Dialog", "Determines the size of the crosshair as a percentage of the screen size (system\n"
"                                variable CURSORSIZE).\n"
"                            "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DisplayTab), _translate("Options_Dialog", "Display"))
        self.groupBox_4.setTitle(_translate("Options_Dialog", "AutoSnap Settings"))
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setToolTip(_translate("Options_Dialog", "Controls the display of the AutoSnap marker. The marker is a geometric symbol that\n"
"                                is displayed when the crosshairs move over a snap point ( AUTOSNAP system variable).\n"
"                            "))
        self.checkBox_AUTOSNAP_DISPLAY_MARK.setText(_translate("Options_Dialog", "Marker"))
        self.pushButton_AutoSnapColor.setToolTip(_translate("Options_Dialog", "Displays the Drawing Window Colors dialog box."))
        self.pushButton_AutoSnapColor.setText(_translate("Options_Dialog", "Colors"))
        self.checkBox_APBOX.setToolTip(_translate("Options_Dialog", "Turns the display of the AutoSnap aperture box on or off.\n"
"                                The aperture box is a box that appears inside the crosshairs when you snap to an object\n"
"                                (APBOX system variable).\n"
"                            "))
        self.checkBox_APBOX.setText(_translate("Options_Dialog", "Display AutoSnap aperture box"))
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setToolTip(_translate("Options_Dialog", "Controls the display of the AutoSnap tooltip. The tooltip is a label that describes\n"
"                                which part of the object you are snapping to (AUTOSNAP system variable).\n"
"                            "))
        self.checkBox_AUTOSNAP_DISPLAY_TOOLTIPS.setText(_translate("Options_Dialog", "Display AutoSnap tooltip"))
        self.checkBox_AUTOSNAP_MAGNET.setToolTip(_translate("Options_Dialog", "Turns the AutoSnap magnet on or off. The magnet is an automatic movement of the\n"
"                                crosshairs that locks the crosshairs onto the nearest snap point (AUTOSNAP system\n"
"                                variable).\n"
"                            "))
        self.checkBox_AUTOSNAP_MAGNET.setText(_translate("Options_Dialog", "Magnet"))
        self.groupBox_5.setTitle(_translate("Options_Dialog", "Alignment Point Acquisition"))
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setToolTip(_translate("Options_Dialog", "Displays tracking vectors automatically when the aperture moves over an object\n"
"                                snap.\n"
"                            "))
        self.radioButton_POLARMODE_AUTO_ACQUIRE.setText(_translate("Options_Dialog", "Automatic"))
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setToolTip(_translate("Options_Dialog", "Displays tracking vectors when you press Shift and move the aperture over an object\n"
"                                snap.\n"
"                            "))
        self.radioButton_POLARMODE_SHIFT_TO_ACQUIRE.setText(_translate("Options_Dialog", "Shift to acquire"))
        self.groupBox_6.setTitle(_translate("Options_Dialog", "AutoSnap Marker Size"))
        self.horizontalSlider_AUTOSNAPSIZE.setToolTip(_translate("Options_Dialog", "Sets the display size for the AutoSnap marker."))
        self.groupBox_7.setTitle(_translate("Options_Dialog", "Aperture Size"))
        self.horizontalSlider_APERTURE.setToolTip(_translate("Options_Dialog", "Sets the display size for the object snap target box, in pixels (APERTURE system\n"
"                                variable).\n"
"                            "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DraftingTab), _translate("Options_Dialog", "Drafting"))
        self.groupBox_8.setTitle(_translate("Options_Dialog", "Pickbox size"))
        self.horizontalSlider_PICKBOX.setToolTip(_translate("Options_Dialog", "Sets the object selection target height, in pixels (PICKBOX system variable).\n"
"                            "))
        self.groupBox_9.setTitle(_translate("Options_Dialog", "Grip size"))
        self.horizontalSlider_GRIPSIZE.setToolTip(_translate("Options_Dialog", "Sets the size of the grip box in pixels ( GRIPSIZE system variable)."))
        self.groupBox_10.setTitle(_translate("Options_Dialog", "Selection modes"))
        self.checkBox_PICKFIRST.setToolTip(_translate("Options_Dialog", "Controls whether you select objects before (noun-verb selection) or after you issue\n"
"                                a command (PICKFIRST system variable).\n"
"                            "))
        self.checkBox_PICKFIRST.setText(_translate("Options_Dialog", "Noun/verb selection"))
        self.checkBox_PICKADD.setToolTip(_translate("Options_Dialog", "Controls whether subsequent selections replace the current selection set or add to\n"
"                                it (PICKADD system variable).\n"
"                            "))
        self.checkBox_PICKADD.setText(_translate("Options_Dialog", "Use Shift to add to selection"))
        self.groupBox_11.setTitle(_translate("Options_Dialog", "Grips"))
        self.button_GripColor.setToolTip(_translate("Options_Dialog", "Displays the Grip Colors dialog box where you can specify the colors for different\n"
"                                grip status and elements.\n"
"                            "))
        self.button_GripColor.setText(_translate("Options_Dialog", "Grip Colors..."))
        self.checkBox_GRIPS.setToolTip(_translate("Options_Dialog", "Controls the display of grips on selected objects. Displaying grips in a drawing\n"
"                                significantly affects performance. Clear this option to optimize performance ( GRIPS\n"
"                                system variable).\n"
"                            "))
        self.checkBox_GRIPS.setText(_translate("Options_Dialog", "Shows grips"))
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setToolTip(_translate("Options_Dialog", "Controls the display of dynamic menu when pausing over a multi-functional grip\n"
"                                (GRIPMULTIFUNCTIONAL system variable).\n"
"                            "))
        self.checkBox_GRIPMULTIFUNCTIONAL_ON_DYNAMIC_MENU_AND_HOT_GRIPT.setText(_translate("Options_Dialog", "Shows dynamic grip menu"))
        self.lineEdit_GRIPOBJLIMIT.setToolTip(_translate("Options_Dialog", "Suppresses the display of grips when the selection set includes more than the\n"
"                                specified number of objects (GRIPOBJLIMIT system variable).\n"
"                            "))
        self.label_GRIPOBJLIMIT.setText(_translate("Options_Dialog", "Object selection limit for display of grips"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SelectionTab), _translate("Options_Dialog", "Selection"))

