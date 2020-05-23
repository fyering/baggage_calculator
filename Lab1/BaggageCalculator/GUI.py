# coding=utf-8
import tkinter
from tkinter import ttk
from tkinter import *
from BaggageCalculator.Package import package
from BaggageCalculator.SpecialPackage import SpecialPackage
from BaggageCalculator.Ticket import Ticket
from BaggageCalculator.Calculator import Calculator
from tkinter import messagebox
class GUI(object):
    packages=[]
    specialpackages=[]
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("托运行李计费器")
        self.root.geometry('600x550')
        self.comvalue1 = tkinter.StringVar()
        self.comvalue2 = tkinter.StringVar()
        self.comvalue3 = tkinter.StringVar()
        self.comvalue4 = tkinter.StringVar()
        self.comvalueL = StringVar()
        self.comvalueW = StringVar()
        self.comvalueH = StringVar()
        self.comvalue_Weight = StringVar()
        self.comvalue_SpecialWeight=StringVar()
        self.comvalue_Info=StringVar()
        self.comvalue_VIPCard=StringVar()
        self.comvalue_special_Info=StringVar()
        self.numOfPackage=0
        self.numOfSpecialPackage=0
        self.label_cockpit_type=tkinter.Label(self.root,text='座舱类型')
        self.label_passenger_type=tkinter.Label(self.root,text='旅客类型')
        self.label_flight_type=tkinter.Label(self.root,text='航班类型')
        self.label_VIPCard=tkinter.Label(self.root,text='VIP')
        self.label_ticket_price=tkinter.Label(self.root,text='票价')
        self.label_annotations=tkinter.Label(self.root,justify = 'left',width=80,wraplength=480,text='区域一：美洲（除美国/加拿大外）/加勒比海地区与欧洲/非洲/中东/亚洲/西南太平洋之间的航线；\n'
                                                            '区域二：欧洲/中东与非洲/亚洲/西南太平洋之间航线；日本与西南太平洋之间航线； 日本/西南太平洋与亚洲（不含日本及西南太平洋）/非洲之间航线；\n'
                                                            '区域三：加拿大与美洲（除美国/加拿大外）/加勒比海地区/欧洲/非洲/中东/亚洲/西南太平洋之间 航线；  \n'
                                                            '区域四：美国（含夏威夷）与美洲（除美国外）/加勒比海地区/欧洲/非洲/中东/亚洲/西南太平洋之间航线； \n'
                                                            '区域五：非洲与亚洲（除日本外)之间航线；欧洲与中东之间航线；亚洲（除日本)内航线； 美洲（除美国/加拿大）及加勒比海地区内航线；上述未列明的航线; ')
        self.input_ticket_price=tkinter.Entry(self.root,width=23,textvariable=self.comvalue4)
        self.comboxlist_cockpit_type=ttk.Combobox(self.root,textvariable=self.comvalue1)
        self.comboxlist_flight_type=ttk.Combobox(self.root,textvariable=self.comvalue2)
        self.comboxlist_passenger_type = ttk.Combobox(self.root, textvariable=self.comvalue3)
        self.comboxlist_VIPCard=ttk.Combobox(self.root,textvariable=self.comvalue_VIPCard)
        self.comboxlist_flight_type["values"]=("国内航线","区域一","区域二","区域三","区域四","区域五")
        self.comboxlist_cockpit_type["values"] = ("头等舱","商务舱","悦享经济舱","超级经济舱", "经济舱")
        self.comboxlist_passenger_type["values"] = ("成人", "儿童","婴儿")
        self.comboxlist_VIPCard["values"]=("无","凤凰知音白金卡","凤凰知音金卡","凤凰知音银卡","星空联盟金卡")
        self.button_package_info=tkinter.Button(self.root,text='添加行李信息',command=self.insert_package,width=20)
        self.button_package_special = tkinter.Button(self.root, text='添加特殊行李', command=self.insert_special_package, width=20)
        self.button_calculate=tkinter.Button(self.root,text='计算',width=30,command=self.calculate_baggage)
        self.listbox_package=tkinter.Listbox(self.root,selectmode=MULTIPLE,height=8,listvariable=self.comvalue_Info)
        self.comboxlist_flight_type.current(0)
        self.comboxlist_cockpit_type.current(0)
        self.comboxlist_passenger_type.current(0)
        self.comboxlist_VIPCard.current(0)
        self.label_ticket_price.place(x=60,y=80)
        self.input_ticket_price.place(x=135,y=80)
        self.label_cockpit_type.place(x=60,y=120)
        self.comboxlist_cockpit_type.place(x=135,y=120)
        self.label_passenger_type.place(x=60, y=160)
        self.comboxlist_passenger_type.place(x=135, y=160)
        self.label_flight_type.place(x=60, y=40)
        self.comboxlist_flight_type.place(x=135, y=40)
        self.label_VIPCard.place(x=60,y=200)
        self.comboxlist_VIPCard.place(x=135,y=200)
        self.button_package_info.place(x=320,y=40)
        self.button_package_special.place(x=320, y=80)
        self.listbox_package.place(x=320,y=120)
        self.button_calculate.place(x=60,y=240)
        self.label_annotations.place(x=30,y=320)
        self.root.mainloop()
    def insert_special_package(self):
        self.top_special = Toplevel()
        self.top_special.title('添加特殊行李')
        self.top_special.geometry('150x200')
        self.label_package_type = tkinter.Label(self.top_special, text='类型')
        self.label_special_package_weight = tkinter.Label(self.top_special, text='重量（kg）')
        self.comboxlist_type = ttk.Combobox(self.top_special, textvariable=self.comvalue_special_Info, width=7)
        self.comboxlist_type["values"] = ("Type1", "Type2", "Type3", "Type4", "Type5", "Type6", "Type7", "Type8", "Type9", "Type10", "Type11", "Type12")
        self.input_special_package_weight = tkinter.Entry(self.top_special, textvariable=self.comvalue_SpecialWeight, width=10)
        self.button_insert = tkinter.Button(self.top_special, text='添加', command=self.addSpecialPackage, width=17)
        self.label_package_type.place(x=10, y=40)
        self.comboxlist_type.place(x=70, y=40)
        self.label_special_package_weight.place(x=10, y=80)
        self.input_special_package_weight.place(x=70, y=80)
        self.button_insert.place(x=10, y=140)
    def addSpecialPackage(self):
        type = self.comvalue_special_Info.get()
        weight = float(self.comvalue_SpecialWeight.get())
        print(weight)
        self.numOfSpecialPackage += 1
        string = "特殊行李" + str(
            self.numOfSpecialPackage) + ":" + self.comvalue_special_Info.get() + "," + self.comvalue_SpecialWeight.get() + "kg"
        Ppackage = SpecialPackage(weight,type)
        self.specialpackages.append(Ppackage)
        self.listbox_package.insert(END, string)
    def insert_package(self):
        self.top=Toplevel()
        self.top.title('添加行李信息')
        self.top.geometry('150x200')
        self.label_package_length=tkinter.Label(self.top,text='长（cm）')
        self.label_package_width = tkinter.Label(self.top, text='宽（cm）')
        self.label_package_height = tkinter.Label(self.top, text='高（cm）')
        self.label_package_weight=tkinter.Label(self.top,text='重量（kg）')
        self.input_package_length=tkinter.Entry(self.top,textvariable=self.comvalueL,width=10)
        self.input_package_width = tkinter.Entry(self.top,textvariable=self.comvalueW,width=10)
        self.input_package_height = tkinter.Entry(self.top,textvariable=self.comvalueH,width=10)
        self.input_package_weight=tkinter.Entry(self.top,textvariable=self.comvalue_Weight,width=10)
        self.button_insert=tkinter.Button(self.top,text='添加',command=self.addpackage,width=17)
        self.label_package_length.place(x=10,y=20)
        self.input_package_length.place(x=70,y=20)
        self.label_package_width.place(x=10,y=50)
        self.input_package_width.place(x=70,y=50)
        self.label_package_height.place(x=10,y=80)
        self.input_package_height.place(x=70,y=80)
        self.label_package_weight.place(x=10,y=110)
        self.input_package_weight.place(x=70,y=110)
        self.button_insert.place(x=10,y=140)
    def addpackage(self):
        l = float(self.comvalueL.get())
        w = float(self.comvalueW.get())
        h = float(self.comvalueH.get())
        weight = float(self.comvalue_Weight.get())
        self.numOfPackage+=1
        string = "行李"+str(self.numOfPackage)+":"+self.comvalueL.get() + "*" + self.comvalueW.get() + "*" + self.comvalueH.get() + "," + self.comvalue_Weight.get() + "kg"
        Ppackage=package(l,w,h,weight)
        self.packages.append(Ppackage)
        self.listbox_package.insert(END,string)


    def calculate_baggage(self):
        cockpitClass, passengerType, price, area, card=self.convert()
        ticket=Ticket(cockpitClass,passengerType,price,area,card)
        calculate=Calculator(ticket,self.packages,self.specialpackages)
        IsOverweight,IsOversize,IsOutOfSize,expense=calculate.calculate()
        if IsOverweight==True or IsOversize==True:
            tkinter.messagebox.showerror('错误','存在超重或超尺寸的单件物品，请您拆分包裹！')
        if IsOutOfSize==True:
            tkinter.messagebox.showerror('错误', '存在不符合规格的行李！')
        string='托运行李费用需'+str(expense)+'RMB!'
        tkinter.messagebox.showinfo('计算结果',string)
        self.listbox_package.delete(0,END)
        self.packages.clear()
        self.specialpackages.clear()
    def convert(self):
        cockpitClass = self.comvalue1.get()
        passengerType = self.comvalue3.get()
        price = float(self.comvalue4.get())
        area = self.comvalue2.get()
        card = self.comvalue_VIPCard.get()
        if cockpitClass=='头等舱':
            cockpitClass='FIRST_CLASS'
        elif cockpitClass=='商务舱':
            cockpitClass='BUSINESS_CLASS'
        elif cockpitClass=='悦享经济舱':
            cockpitClass='ENJOY_ECONOMY_CLASS'
        elif cockpitClass=='超级经济舱':
            cockpitClass='SUPER_ECONOMY_CLASS'
        else:
            cockpitClass='ECONOMY_CLASS'
        if area =='国内航线':
            area='AREA0'
        elif area == '区域一':
            area = 'AREA1'
        elif area == '区域二':
            area = 'AREA2'
        elif area == '区域三':
            area = 'AREA3'
        elif area == '区域四':
            area = 'AREA4'
        else:
            area='AREA5'
        if passengerType=='成人':
            passengerType='ADULT'
        elif passengerType=='儿童':
            passengerType='CHILDREN'
        else:
            passengerType='INFANCY'
        if card == '无':
            card = 'None'
        elif card == '凤凰知音白金卡':
            card = 'PLATINUM'
        elif card == '凤凰知音金卡':
            card = 'GOLD'
        elif card == '凤凰知音银卡':
            card = 'SILVER'
        else:
            card = 'STAR_ALLIANCE_GOLD'
        return cockpitClass,passengerType,price,area,card


