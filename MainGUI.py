# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subWidget
from PyQt5.QtGui import QStandardItem,QStandardItemModel
from PyQt5.QtWidgets import QMessageBox
import rule
import re

class Ui_widget(object):
    def setupUi(self, widget):
        self.Widget=widget
        widget.setObjectName("widget")
        widget.resize(730, 602)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1239651.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")
        self.airline = QtWidgets.QComboBox(widget)
        self.airline.setGeometry(QtCore.QRect(90, 20, 91, 16))
        self.airline.setObjectName("airline")
        self.airline.addItem("")
        self.airline.addItem("")
        self.airline.addItem("")
        self.airline.addItem("")
        self.airline.addItem("")
        self.airline.addItem("")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 41, 9))
        self.label_2.setObjectName("label_2")
        # self.start = QtWidgets.QLineEdit(widget)
        # self.start.setGeometry(QtCore.QRect(90, 60, 91, 21))
        # self.start.setObjectName("start")
        ####
        self.start = QtWidgets.QComboBox(widget)
        self.start.setGeometry(QtCore.QRect(90, 60, 91, 21))
        self.start.setObjectName("start")
        self.start.addItem("")
        self.start.addItem("")
        self.start.addItem("")
        self.start.addItem("")

        ####
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 41, 9))
        self.label_3.setObjectName("label_3")
        self.jicang = QtWidgets.QComboBox(widget)
        self.jicang.setGeometry(QtCore.QRect(90, 100, 91, 16))
        self.jicang.setObjectName("jicang")
        self.jicang.addItem("")
        self.jicang.addItem("")
        self.jicang.addItem("")
        self.jicang.addItem("")
        self.jicang.addItem("")
        self.jicang.addItem("")
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 41, 9))
        self.label_4.setObjectName("label_4")
        self.kepiaotype = QtWidgets.QComboBox(widget)
        self.kepiaotype.setGeometry(QtCore.QRect(90, 136, 91, 16))
        self.kepiaotype.setObjectName("kepiaotype")
        self.kepiaotype.addItem("")
        self.kepiaotype.addItem("")
        self.kepiaotype.addItem("")
        self.label_5 = QtWidgets.QLabel(widget)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 41, 9))
        self.label_5.setObjectName("label_5")
        # self.huiyuan = QtWidgets.QComboBox(widget)
        # self.huiyuan.setGeometry(QtCore.QRect(90, 170, 91, 16))
        # self.huiyuan.setObjectName("huiyuan")
        # self.huiyuan.addItem("")
        # self.huiyuan.addItem("")
        # self.huiyuan.addItem("")
        # self.huiyuan.addItem("")
        # self.huiyuan.addItem("")
        # self.huiyuan.addItem("")
        self.label_6 = QtWidgets.QLabel(widget)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 41, 9))
        self.label_6.setObjectName("label_6")
        self.price = QtWidgets.QLineEdit(widget)
        self.price.setGeometry(QtCore.QRect(90, 200, 91, 16))
        self.price.setObjectName("price")
        self.price.setText("1111")
        self.add = QtWidgets.QPushButton(widget)
        self.add.setGeometry(QtCore.QRect(20, 240, 161, 21))
        self.add.setObjectName("add")
        self.baggage = QtWidgets.QListView(widget)
        self.baggage.setGeometry(QtCore.QRect(230, 0, 321, 271))
        self.baggage.setObjectName("baggage")
        self.delbaggage=QtWidgets.QPushButton(widget)
        self.delbaggage.setGeometry(QtCore.QRect(552, 0, 161, 21))
        self.delbaggage.setObjectName("del")
        self.confirm = QtWidgets.QPushButton(widget)
        self.confirm.setGeometry(QtCore.QRect(130, 280, 311, 16))
        self.confirm.setObjectName("confirm")
        self.label_7 = QtWidgets.QLabel(widget)
        self.label_7.setGeometry(QtCore.QRect(30, 320, 401, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(widget)
        self.label_8.setGeometry(QtCore.QRect(30, 340, 521, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(widget)
        self.label_9.setGeometry(QtCore.QRect(30, 359, 441, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(widget)
        self.label_10.setGeometry(QtCore.QRect(30, 380, 431, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(widget)
        self.label_11.setGeometry(QtCore.QRect(30, 400, 441, 21))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)
        self.confirm.clicked.connect(self.getvalue)
        self.add.clicked.connect(self.setBaggage)
        self.delbaggage.clicked.connect(self.deleteRow)
        self.model = QStandardItemModel()#用于向列表添加行李信息
        self.total_bag=[]#列表用于存放行李
        item_str = "重量:" + "31" + " 长:" + "30" + " 宽:" + "30" + " 高:" + "30" + " 特殊行李:" + "否" + " 类型:" + "无" + " 免费额:" + "无"
        self.total_bag.append(item_str)
        item = QStandardItem(item_str)
        self.model.appendRow(item)
        self.baggage.setModel(self.model)
    def deleteRow(self):
        selected = self.baggage.selectedIndexes()
        itemmodel=self.baggage.model()
        for i in selected:
            itemmodel.removeRow(i.row())
            self.total_bag.remove(self.total_bag[i.row()])


    def getvalue(self):
        self.airline_value=self.airline.currentText()#航线区域类型
        self.start_value=self.start.currentText()#始发航站
        self.jicang_value=self.jicang.currentText()#机舱类型
        self.kepiaotype_value=self.kepiaotype.currentText()#客票类型
        self.price_value=self.price.text()#票价

        if self.airline_value=='国内'and (self.jicang_value=='豪华头等舱'or self.jicang_value=='悦享经济舱'or self.jicang_value=='超级经济舱' ):
            reply = QMessageBox.about(self.Widget, "提示", "国内航班无豪华头等舱、悦享经济舱、超级经济舱")
        elif self.price_value=='':
            reply = QMessageBox.about(self.Widget, "提示", "请填写机票价格")
        else:
            print(self.airline_value)
            Rule=rule.rule(self.total_bag,self.airline_value,self.start_value,self.jicang_value,self.kepiaotype_value,self.price_value)

            result=Rule.error_dealer()

            if result=='free':
                reply = QMessageBox.about(self.Widget, "结果", "免费")
            elif result=='error':
                reply = QMessageBox.about(self.Widget, "提示", "填写格式错误")
            elif result=='ok':
                res,dw=Rule.count_dollar()
                if res==0:
                    reply = QMessageBox.about(self.Widget, "结果", "免费")
                elif res==-1:
                    reply = QMessageBox.about(self.Widget, "结果", "不能托运")
                else:
                    reply = QMessageBox.about(self.Widget, "结果", str(res)+dw)


        #print(self.airline_value,self.start_value,self.jicang_value,self.kepiaotype_value,self.huiyuan_value,self.price_value)
        print(self.total_bag)
    def setBaggage(self):#打开设置行李详细信息的子窗口
        self.baggage_widget = subWidget.Ui_Form()
        self.widget = QtWidgets.QWidget()
        self.baggage_widget.setupUi(self.widget)
        self.widget.show()
        self.baggage_widget.confirm.clicked.connect(self.deliver_value)

    def getBaggage(self):#获取子窗口的信息
        self.weight_value = self.baggage_widget.weight.text()
        self.long_value = self.baggage_widget.long_2.text()
        self.width_value = self.baggage_widget.width.text()
        self.height_value = self.baggage_widget.height.text()
        self.special_or_not = self.baggage_widget.special.currentText()
        self.stype_value = self.baggage_widget.stype.currentText()
        self.free_value = self.baggage_widget.free.currentText()
        if self.special_or_not=="否":
            self.free_value='无'
            self.stype_value='无'
        item_str="重量:"+self.weight_value+" 长:"+self.long_value+" 宽:"+self.width_value+" 高:"+self.height_value+" 特殊行李:"+self.special_or_not+" 类型:"+self.stype_value+" 免费额:"+self.free_value
        self.total_bag.append(item_str)
        item=QStandardItem(item_str)
        self.model.appendRow(item)
        self.baggage.setModel(self.model)

        #print(self.weight_value,self.long_value,self.width_value,self.height_value,self.special_or_not,self.stype_value,self.free_value)
    def deliver_value(self):
        self.airline_value = self.airline.currentText()  # 航线区域类型
        self.start_value = self.start.currentText()  # 始发航站
        self.jicang_value = self.jicang.currentText()  # 机舱类型
        self.kepiaotype_value = self.kepiaotype.currentText()  # 客票类型
        self.price_value = self.price.text()  # 票价
        weight_value = self.baggage_widget.weight.text()
        long_value = self.baggage_widget.long_2.text()
        width_value = self.baggage_widget.width.text()
        height_value = self.baggage_widget.height.text()
        special_or_not = self.baggage_widget.special.currentText()
        stype_value = self.baggage_widget.stype.currentText()
        free_value = self.baggage_widget.free.currentText()

        pattern = re.compile("[^\d\.]")  # 查找非数字
        result1 = pattern.findall(str(weight_value))
        result2=pattern.findall(str(long_value))
        result3 = pattern.findall(str(width_value))
        result4 = pattern.findall(str(height_value))



        if weight_value=='' or long_value==''or width_value==''or height_value=='' or result1!=[] or result2!=[] or result3!=[] or result4!=[]:
            reply=QMessageBox.about(self.widget,"提示","填写格式不正确")
        elif float(long_value)==0 or float(width_value)==0 or float(height_value)==0:
            reply = QMessageBox.about(self.widget, "提示", "不符合托运条件")
        else:
            total_length = float(long_value) + float(width_value) + float(height_value)
            if (self.airline_value=='国内' and special_or_not=='否' and (float(long_value)>100  or float(width_value)>60 or float(height_value)>40)):
                reply = QMessageBox.about(self.widget, "提示", "不符合托运条件！")
            elif self.airline_value!='国内' and special_or_not=='否' and (total_length>203):
                reply = QMessageBox.about(self.widget, "提示", "不符合托运条件！")
            elif (special_or_not=='否')and((float(weight_value)<2 or float(weight_value)>32)):
                reply=QMessageBox.about(self.widget,"提示","不符合托运条件！")
            elif(special_or_not=='是' and free_value=='是' and (float(weight_value)<2 or float(weight_value)>32)):
                reply = QMessageBox.about(self.widget, "提示", "不符合托运条件！")
            elif (special_or_not == '是' and free_value == '否' and (float(weight_value) < 2 or float(weight_value) > 45)):
                reply = QMessageBox.about(self.widget, "提示", "不符合托运条件！")
            elif special_or_not=='是'and(stype_value=='无' or free_value=='无'):
                reply = QMessageBox.about(self.widget, "提示", "请选择特殊类型或者是否计入免费行李额")


            else:
                self.widget.close()#子窗口的关闭
                self.getBaggage()

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "行李计算器"))
        self.label.setText(_translate("widget", "航线区域类型"))
        self.airline.setCurrentText(_translate("widget", "国内"))
        self.airline.setItemText(0, _translate("widget", "国内"))
        self.airline.setItemText(1, _translate("widget", "区域一"))
        self.airline.setItemText(2, _translate("widget", "区域二"))
        self.airline.setItemText(3, _translate("widget", "区域三"))
        self.airline.setItemText(4, _translate("widget", "区域四"))
        self.airline.setItemText(5, _translate("widget", "区域五"))
        self.label_2.setText(_translate("widget", "始发航站"))
        self.label_3.setText(_translate("widget", "机舱"))

        self.start.setItemText(0, _translate("widget", "国内"))
        self.start.setItemText(1, _translate("widget", "加拿大"))
        self.start.setItemText(2, _translate("widget", "欧元区"))
        self.start.setItemText(3, _translate("widget", "其他"))

        self.jicang.setItemText(0, _translate("widget", "公务舱"))
        self.jicang.setItemText(1, _translate("widget", "头等舱"))
        self.jicang.setItemText(2, _translate("widget", "豪华头等舱"))
        self.jicang.setItemText(3, _translate("widget", "悦享经济舱"))
        self.jicang.setItemText(4, _translate("widget", "超级经济舱"))
        self.jicang.setItemText(5, _translate("widget", "经济舱"))
        self.label_4.setText(_translate("widget", "客票类型"))
        self.kepiaotype.setItemText(0, _translate("widget", "成人票"))
        self.kepiaotype.setItemText(1, _translate("widget", "儿童票"))
        self.kepiaotype.setItemText(2, _translate("widget", "婴儿票"))
        # self.label_5.setText(_translate("widget", "会员"))
        # self.huiyuan.setItemText(0, _translate("widget", "无"))
        # self.huiyuan.setItemText(1, _translate("widget", "凤凰知音终身白金卡"))
        # self.huiyuan.setItemText(2, _translate("widget", "凤凰知音白金卡"))
        # self.huiyuan.setItemText(3, _translate("widget", "凤凰知音金卡"))
        # self.huiyuan.setItemText(4, _translate("widget", "凤凰知音银卡"))
        # self.huiyuan.setItemText(5, _translate("widget", "星空联盟金卡"))
        self.label_6.setText(_translate("widget", "票价(元)"))
        self.add.setText(_translate("widget", "添加行李"))
        self.delbaggage.setText(_translate("widget", "删除"))
        self.confirm.setText(_translate("widget", "确认"))
        self.label_7.setText(_translate("widget", "区域一;美洲（除美国/加拿大外）/加勒比海地区与欧洲/非洲/中东/亚洲/西南太平洋之间的航线；"))
        self.label_8.setText(_translate("widget", "区域二：欧洲/中东与非洲/亚洲/西南太平洋之间航线；日本与西南太平洋之间航线；日本/西南太平洋与亚洲\n"
"（不含日本及西南太平洋）/非洲之间航线"))
        self.label_9.setText(_translate("widget", "区域三：加拿大与美洲（除美国/加拿大外）/加勒比海地区/欧洲/非洲/中东/亚洲/西南太平洋之间航线；"))
        self.label_10.setText(_translate("widget", "区域四：美国（含夏威夷）与美洲（除美国外）/加勒比海地区/欧洲/非洲/中东/亚洲/西南太平洋之间航线；"))
        self.label_11.setText(_translate("widget", "区域五:非洲与亚洲（除日本外)之间航线；欧洲与中东之间航线；亚洲（除日本)内航线；美洲（除美国/加拿大）及加勒比海地区内航线；\n"
"上述未列明的航线"))
if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    new = Ui_widget()
    new.setupUi(widget)
    widget.show()
    sys.exit(app.exec())
