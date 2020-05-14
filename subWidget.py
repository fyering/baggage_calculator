# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1239651.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 41, 9))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 41, 9))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.label_3.setObjectName("label_3")
        self.weight = QtWidgets.QLineEdit(Form)
        self.weight.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.weight.setObjectName("weight")
        self.long_2 = QtWidgets.QLineEdit(Form)
        self.long_2.setGeometry(QtCore.QRect(60, 60, 113, 20))
        self.long_2.setObjectName("long_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 101, 21))
        self.label_5.setObjectName("label_5")
        self.stype = QtWidgets.QComboBox(Form)
        self.stype.setGeometry(QtCore.QRect(130, 210, 91, 16))
        self.stype.setObjectName("stype")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.stype.addItem("")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(250, 20, 300, 300))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 41, 9))
        self.label_7.setObjectName("label_7")
        self.width = QtWidgets.QLineEdit(Form)
        self.width.setGeometry(QtCore.QRect(60, 90, 113, 20))
        self.width.setObjectName("width")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 41, 9))
        self.label_8.setObjectName("label_8")
        self.height = QtWidgets.QLineEdit(Form)
        self.height.setGeometry(QtCore.QRect(60, 120, 113, 20))
        self.height.setObjectName("height")
        self.redo = QtWidgets.QPushButton(Form)
        self.redo.setGeometry(QtCore.QRect(30, 360, 151, 31))
        self.redo.setObjectName("redo")
        self.confirm = QtWidgets.QPushButton(Form)
        self.confirm.setGeometry(QtCore.QRect(240, 360, 151, 31))
        self.confirm.setObjectName("confirm")
        self.special = QtWidgets.QComboBox(Form)
        self.special.setGeometry(QtCore.QRect(120, 160, 81, 16))
        self.special.setObjectName("special")
        self.special.addItem("")
        self.special.addItem("")
        self.free = QtWidgets.QComboBox(Form)
        self.free.setGeometry(QtCore.QRect(130, 240, 91, 16))
        self.free.setObjectName("free")
        self.free.addItem("")
        self.free.addItem("")
        self.free.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.redo.clicked.connect(self.redoall)


    def redoall(self):
        self.weight.clear()
        self.long_2.clear()
        self.width.clear()
        self.height.clear()




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "行李详细信息"))
        self.label.setText(_translate("Form", "重量(kg)"))
        self.label_2.setText(_translate("Form", "长(cm)"))
        self.label_3.setText(_translate("Form", "是否为特殊行李"))
        self.label_4.setText(_translate("Form", "特殊行李类型"))
        self.label_5.setText(_translate("Form", "是否计入免费行李额"))
        self.stype.setItemText(0, _translate("Form", "无"))
        self.stype.setItemText(1, _translate("Form", "类型1"))
        self.stype.setItemText(2, _translate("Form", "类型2(计入免费额)"))
        self.stype.setItemText(3, _translate("Form", "类型3"))
        self.stype.setItemText(4, _translate("Form", "类型4"))
        self.stype.setItemText(5, _translate("Form", "类型5(计入免费额)"))
        self.stype.setItemText(6, _translate("Form", "类型6"))
        self.stype.setItemText(7, _translate("Form", "类型7"))
        self.stype.setItemText(8, _translate("Form", "类型8"))
        self.stype.setItemText(9, _translate("Form", "类型9"))
        self.stype.setItemText(10, _translate("Form", "类型10"))


        self.label_6.setText(_translate("Form", "类型1：可免费运输的特殊行李\n"
"类型2：高尔夫球包、保龄球、滑翔伞/降落伞、滑雪/滑水用具\n（不包括雪橇/水撬）、轮滑/滑板用具、潜水用具、射箭用具、曲棍球用具、冰球用具、网球用具、登山用具、自行车\n类型3：皮划艇/独木舟、悬挂式滑翔运动用具、雪橇/水撬\n冲浪板、风帆冲浪用具、橡皮艇或船\n"
                                                "类型4：撑杆、标枪、单独包装的划船用具或浆、骑马用具\n类型5：睡袋、背包、野营用具、渔具、乐器、辅助设备（非残疾、\n伤、病旅客托运）、可折叠婴儿床、可折叠婴儿车或婴儿\n摇篮或婴儿汽车安全座椅（非婴儿旅客托运）\n"
                                                "类型6：小型电器或仪器、媒体设备\n类型7：可作为行李运输的枪支 \n类型8:可作为行李运输的子弹 \n类型9:小动物（仅限家庭驯养的猫、狗）\n注：每个容器的总重量（包括其中的小动物及水与食物的重量）\n注：只有类型二和类型五参与免费行李额\n"
                                                "计入免费行李额的特殊行李重量范围为[2kg,32kg],超过32kg的行李请拆分\n"
                                                "不计入免费行李额的特殊行李重量范围在[2kg,45kg],超过45kg的行李请拆分\n"
                                                "普通行李的重要范围在[2kg,32kg],\n长宽高之和范围为[60,203],如超过请自行拆分"))
        self.label_7.setText(_translate("Form", "宽(cm)"))
        self.label_8.setText(_translate("Form", "高(cm)"))
        self.redo.setText(_translate("Form", "重置"))
        self.confirm.setText(_translate("Form", "确定"))
        self.special.setItemText(0, _translate("Form", "是"))
        self.special.setItemText(1, _translate("Form", "否"))
        self.free.setItemText(0, _translate("Form", "无"))
        self.free.setItemText(1, _translate("Form", "是"))
        self.free.setItemText(2, _translate("Form", "否"))
