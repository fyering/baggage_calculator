import operator
PassengerType={'ADULT','CHILDREN','INFANCY'}
CockpitType={'FIRST_CLASS','BUSINESS_CLASS','ENJOY_ECONOMY_CLASS','SUPER_ECONOMY_CLASS','ECONOMY_CLASS'}
FlightArea={'AREA0','AREA1','AREA2','AREA3','AREA4','AREA5'}
SpecialBaggage={'TYPE1','TYPE2','TYPE3','TYPE4','TYPE5','TYPE6','TYPE7','TYPE8','TYPE9','TYPE10','TYPE11','TYPE12'}
VIPCard={'None','PLATINUM','GOLD','SILVER','STAR_ALLIANCE_GOLD'}

class Calculator(object):
    def __init__(self,Ticket,Packages=None,SpecialPackages=None):
        self.Packages=Packages
        self.Ticket=Ticket
        self.SpecialPackages=SpecialPackages
    def calculate(self):
        IsOverweight=False
        IsOversize=False
        IsOutOfSize=False
        expense=0.0

        if self.Packages is not None:
            if self.Ticket.getArea()=='AREA0':
                IsOverweight,IsOversize,IsOutOfSize,expense=self.domestic_flight_calculate()
            else:
                IsOverweight,IsOversize,IsOutOfSize,expense=self.international_flight_calculate()
        if self.SpecialPackages is not None:
            special_weight,special_size,special_expense=self.special_baggage_calculate()
            IsOverweight=IsOverweight or special_weight
            IsOutOfSize=IsOutOfSize or special_size
            expense +=special_expense
        return IsOverweight,IsOversize,IsOutOfSize,expense
    def domestic_flight_calculate(self):
        cmpfun = operator.attrgetter('weight')
        self.Packages.sort(key=cmpfun, reverse=True)
        cockpit=self.Ticket.getCockpitClass()
        passenger=self.Ticket.getPassengerType()
        price=self.Ticket.getPrice()
        flag=False   #判断是否直接逾重计费
        IsOverweight=False
        IsOversize=False
        IsOutOfSize=False
        sum=0.0
        expense=0.0
        extraNum=0
        extraWeight=0.0
        if self.Ticket.getCard()=='PLATINUM':
            extraNum=1
            extraWeight=30
        if self.Ticket.getCard()=='GOLD' or self.Ticket.getCard()=='SILVER' or self.Ticket.getCard()=='STAR_ALLIANCE_GOLD':
            extraNum = 1
            extraWeight = 20
        for package in self.Packages:

            length=package.getLength()
            width=package.getWidth()
            height=package.getHeight()
            weight = package.getWeight()
            print(weight)
            sum += weight
            if length+width+height>203:
                IsOversize=True
                print("存在超尺寸物品，请您拆分包裹")
            if weight>32:
                IsOverweight=True
                print("存在超重物品，请您拆分包裹。")
            if weight<2 or length+width+height<60:
                IsOutOfSize=True
                print("存在不符合重量或尺寸的物品")
            if IsOversize==True or IsOverweight==True or IsOutOfSize==True:
                return IsOverweight,IsOversize,IsOutOfSize,expense
            if extraNum!=0 and weight <= extraWeight:
                print('VIP Card特权')
                sum-=weight
                extraNum-=1
                continue
            if flag==True:
                print("对当前物品进行逾重计费")
                expense+=weight*price*0.015
                continue
            if passenger=='INFANCY':
                if sum >= 10:
                    print("婴儿免费托运行李10kg，对超出部分逾重计费。")
                    expense+=(sum-10)*price*0.015
                    flag=True
                    continue

            if cockpit=="FIRST_CLASS" and sum >= 40:
                print("对超出部分进行逾重计费")
                expense += (sum - 40) * price * 0.015
                flag=True
                continue

            if cockpit == "BUSINESS_CLASS" and sum >= 30:
                print("对超出部分进行逾重计费")
                expense += (sum - 30) * price * 0.015
                flag = True
                continue

            if (cockpit == "ECONOMY_CLASS" or cockpit=="ENJOY_ECONOMY_CLASS" or cockpit=="SUPER_ECONOMY_CLASS") and sum >= 20:
                print("对超出部分进行逾重计费")
                expense += (sum - 20) * price * 0.015
                flag = True
                continue
        return IsOverweight,IsOversize,IsOutOfSize,expense
    def international_flight_calculate(self):
        cmpfun=operator.attrgetter('weight')
        self.Packages.sort(key=cmpfun,reverse=True)
        cockpit = self.Ticket.getCockpitClass()    #座舱类型
        passenger = self.Ticket.getPassengerType() #乘客类型
        FlightArea=self.Ticket.getArea()           #航班区域
        numberOfpackages=0
        free_numberOfpackages=2
        expense=0.0
        IsOverweight = False
        IsOversize = False
        IsOutOfSize = False
        if cockpit=='ECONOMY_CLASS' and (FlightArea=='AREA1' or FlightArea=='AREA2'):
            free_numberOfpackages=1
        for package in self.Packages:
            length = package.getLength()
            width = package.getWidth()
            height = package.getHeight()
            weight=package.getWeight()
            sum = length + width + height
            if weight>32 :
                IsOverweight=True
                print("存在单件重量超标的物品，请您拆分包裹。")
            if sum>203:
                IsOversize=True
                print("存在尺寸超标的物品，请您拆分包裹。")
            if weight<2 or sum<60:
                IsOutOfSize = True
                print("存在不符合重量或尺寸的物品")
            if IsOversize==True or IsOverweight==True or IsOutOfSize==True:
                return IsOverweight,IsOversize,IsOutOfSize,expense
            numberOfpackages+=1
            temp=numberOfpackages-free_numberOfpackages
            if FlightArea == 'AREA1':
                if sum <= 158:
                    if(cockpit=='ECONOMY_CLASS' or cockpit=='ENJOY_ECONOMY_CLASS' or cockpit == 'SUPER_ECONOMY_CLASS'):
                        if weight>23 and weight<=28:
                            expense+=380
                        if weight>28 and weight<=32:
                            expense+=980
                else:
                    if weight>2 and weight<=23:
                        expense+=980
                    if weight>23 and weight<=32:
                        expense+=1400
                if temp<=0:
                    print('免费托运')
                elif temp == 1:
                    expense += 1400
                elif temp==2:
                    expense += 2000
                else:
                    expense += 3000
            elif FlightArea == 'AREA2':
                if sum <= 158:
                    if(cockpit=='ECONOMY_CLASS' or cockpit=='ENJOY_ECONOMY_CLASS' or cockpit == 'SUPER_ECONOMY_CLASS'):
                        if weight>23 and weight<=28:
                            expense+=280
                        if weight>28 and weight<=32:
                            expense+=690
                else:
                    if weight>2 and weight<=23:
                        expense+=690
                    if weight>23 and weight<=32:
                        expense+=1100
                if temp<=0:
                    print("免费托运")
                elif temp <3:
                    expense += 1100
                else:
                    expense += 1590
            elif FlightArea == 'AREA3':
                if sum <= 158:
                    if(cockpit=='ECONOMY_CLASS' or cockpit=='ENJOY_ECONOMY_CLASS' or cockpit == 'SUPER_ECONOMY_CLASS'):
                        expense+=520
                else:
                    expense+=520
                if temp<=0:
                    print("免费托运")
                elif temp <3:
                    expense += 1170
                else:
                    expense += 1590
            elif FlightArea == 'AREA4':
                if sum <= 158:
                    if(cockpit=='ECONOMY_CLASS' or cockpit=='ENJOY_ECONOMY_CLASS' or cockpit == 'SUPER_ECONOMY_CLASS'):
                        if weight>23 and weight<=28:
                            expense+=690
                        if weight>28 and weight<=32:
                            expense+=1040
                else:
                    if weight>2 and weight<=23:
                        expense+=1040
                    if weight>23 and weight<=32:
                        expense+=2050
                if temp<=0:
                    print("免费托运")
                elif temp <3:
                    expense += 1380
                else:
                    expense += 1590
            elif FlightArea == 'AREA5':
                if sum <= 158:
                    if(cockpit=='ECONOMY_CLASS' or cockpit=='ENJOY_ECONOMY_CLASS' or cockpit == 'SUPER_ECONOMY_CLASS'):
                        if weight>23 and weight<=28:
                            expense+=210
                        if weight>28 and weight<=32:
                            expense+=520
                else:
                    if weight>2 and weight<=23:
                        expense+=520
                    if weight>23 and weight<=32:
                        expense+=830
                if temp<=0:
                    print("免费托运")
                elif temp ==1:
                    expense += 830
                elif temp ==2:
                    expense += 1100
                else:
                    expense += 1590
            else:
                print("区域选择错误")
        return IsOverweight,IsOversize,IsOutOfSize,expense
    def special_baggage_calculate(self):
        expense=0.0
        IsOverweight=False
        IsOutOfSize=False
        for package in self.SpecialPackages:
            print(package.getWeight())
            if package.getWeight()<2:
                print('不符合运输重量')
                IsOutOfSize=True
            if package.getType()=='Type1' or package.getType()=='Type2' or package.getType()=='Type3' or package.getType()=='Type4':
                print('特殊行李免费运输')
            elif package.getType()=='Type5' or package.getType()=='Type8':
                print('超出免费行李额（件数、重量）部分，须按附件3《国航 实际承运航班一般托运行李超限额收费标准一览表》中对 应标准收取相应费用。超尺寸不另行收费。 ')
            elif package.getType()=='Type6':
                weight=package.getWeight()
                if weight>=2 and weight<=23:
                    expense+=2600
                elif weight>23 and weight<=32:
                    expense+=3900
                elif weight>32 and weight<=45:
                    expense+=5200
                else:
                    IsOverweight=True
            elif package.getType()=='Type7':
                weight = package.getWeight()
                if weight >= 2 and weight <= 23:
                    expense += 1300
                elif weight > 23 and weight <= 32:
                    expense += 2600
                elif weight > 32 and weight <= 45:
                    expense += 3900
                else:
                    IsOverweight = True
            elif package.getType()=='Type9':
                weight = package.getWeight()
                if weight >= 2 and weight <= 23:
                    expense += 490
                elif weight > 23 and weight <= 32:
                    expense += 3900
                else:
                    IsOverweight = True
            elif package.getType()=='Type10':
                weight = package.getWeight()
                if weight >= 2 and weight <= 23:
                    expense += 1300
                elif weight > 23 and weight <= 32:
                    expense += 2600
                else:
                    IsOverweight = True

            elif package.getType() == 'Type11':
                weight = package.getWeight()
                if weight >= 2 and weight <= 5:
                    expense += 1300
            elif package.getType() == 'Type12':
                weight = package.getWeight()
                if weight >= 2 and weight <= 8:
                    expense += 3900
                elif weight > 8 and weight <= 23:
                    expense += 5200
                elif weight > 23 and weight <= 32:
                    expense += 7800
                else:
                    IsOverweight = True
            else:
                print('类型选择错误')
        return IsOverweight,IsOutOfSize,expense



















