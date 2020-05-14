import numpy as np
import re
class rule():

    def __init__(self,bagList,airline,start,cabin,Ttype,price):
        self.airline_area=airline
        self.start=start
        self.cabin_type=cabin
        self.Ticket_type=Ttype
        self.price=price
        self.Baggage_list=self.baggage_dealer(bagList)
        self.bag_num=len(self.Baggage_list)

    def error_dealer(self):
        if(self.Baggage_list==[]):
            return "free"
        pattern = re.compile("[^\d\.]")  # 查找非数字
        result=pattern.findall(str(self.price))
        if result!=[]:
            return "error"
        else:
            return "ok"
    def baggage_dealer(self,baggage_list):
        list=[]
        for bag in baggage_list:
            t_list=[]
            temp_list=str(bag).split(' ')
            weight=temp_list[0].split(':')[1]
            long=temp_list[1].split(':')[1]
            width=temp_list[2].split(':')[1]
            height=temp_list[3].split(':')[1]
            special=temp_list[4].split(':')[1]
            type=temp_list[5].split(':')[1]
            free=temp_list[6].split(':')[1]
            t_list=[weight,long,width,height,special,type,free]
            list.append(t_list)
        return list
    def count_dollar(self):
        total_weight=0
        total_pay=0
        for i in range(self.bag_num):
            if self.Baggage_list[i][4]=='否' or (self.Baggage_list[i][4]=='是'and self.Baggage_list[i][6]=='是'):#普通行李和计入免费托运额的特殊行李
                total_weight+=float(self.Baggage_list[i][0])

        if self.airline_area=='国内':
            if self.Ticket_type=='成人票'or self.Ticket_type=='儿童票':
                if self.cabin_type=='头等舱':
                    if total_weight<=40:
                        total_pay+=0
                    else:
                        total_pay+=round((total_weight-40)*float(self.price)*0.015)

                elif self.cabin_type=='公务舱':
                    if total_weight<=30:
                        total_pay+=0
                    else:
                        total_pay+=round((total_weight-30)*float(self.price)*0.015)

                else: #self.cabin_type=='经济舱':
                    if total_weight<=20:
                        total_pay+=0
                    else:
                        total_pay+=round((total_weight-20)*float(self.price)*0.015)

            else: #self.Ticket_type=='婴儿票':
                if total_weight <= 10:
                    total_pay+=0
                else:
                    total_pay+=round((total_weight - 10) * float(self.price) * 0.015)
        else:
            if self.airline_area=='区域一':
                if self.cabin_type == '头等舱' or self.cabin_type == '公务舱' or self.cabin_type=='豪华头等舱':
                    count=-1
                    if self.Ticket_type == '成人票' or self.Ticket_type == '儿童票':
                        count = 2
                    else:
                        count = 0

                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1400
                        elif count == -1:
                            total_pay += 2000
                        elif count <= -2:
                            total_pay += 3000
                        if self.Baggage_list[i][4] == '否':  # 普通行李的尺寸超了
                            if (float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))>=158 and(float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))<=203:
                                total_pay+=980
                        count=count-1
                elif self.cabin_type == '悦享经济舱' or self.cabin_type == '超级经济舱' or self.cabin_type=='经济舱':
                    count=2
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1400
                        elif count == -1:
                            total_pay += 2000
                        elif count <= -2:
                            total_pay += 3000
                        w=float(self.Baggage_list[i][0])
                        s=float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3])
                        if self.Baggage_list[i][4] == '否':#一般行李
                            if w<=23 and s<=203 and s>158:
                                total_pay+=980
                            elif w<=32 and w>23 and s<=203 and s>158:
                                total_pay+=1400
                            elif w<=32 and w>28 and s<=158 and s>=60:
                                total_pay+=980
                            elif w<=28 and w>23 and s<=158 and s>=60:
                                total_pay+=380
                        elif self.Baggage_list[i][4] == '是' and self.Baggage_list[i][6] =='是':#计入免费额的特殊行李
                            if w<=32 and w>28:
                                total_pay+=980
                            elif w<=28 and w>23:
                                total_pay+=380
                        count=count-1

            elif self.airline_area=='区域二':
                if self.cabin_type == '头等舱' or self.cabin_type == '公务舱' or self.cabin_type=='豪华头等舱':
                    count=-1
                    if self.Ticket_type == '成人票' or self.Ticket_type == '儿童票':
                        count = 2
                    else:
                        count = 0

                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1100
                        elif count == -1:
                            total_pay += 1100
                        elif count <= -2:
                            total_pay += 1590
                        if self.Baggage_list[i][4] == '否':  # 普通行李的尺寸超了
                            if (float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))>=158 and(float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))<=203:
                                total_pay+=690
                        count=count-1
                elif self.cabin_type == '悦享经济舱' or self.cabin_type == '超级经济舱' or self.cabin_type=='经济舱':
                    count=2
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1100
                        elif count == -1:
                            total_pay += 1100
                        elif count <= -2:
                            total_pay += 1590
                        w=float(self.Baggage_list[i][0])
                        s=float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3])
                        if self.Baggage_list[i][4] == '否':#一般行李
                            if w<=23 and s<=203 and s>158:
                                total_pay+=690
                            elif w<=32 and w>23 and s<=203 and s>158:
                                total_pay+=1100
                            elif w<=32 and w>28 and s<=158 and s>=60:
                                total_pay+=690
                            elif w<=28 and w>23 and s<=158 and s>=60:
                                total_pay+=280
                        elif self.Baggage_list[i][4] == '是' and self.Baggage_list[i][6] =='是':#计入免费额的特殊行李
                            if w<=32 and w>28:
                                total_pay+=690
                            elif w<=28 and w>23:
                                total_pay+=280
                        count=count-1

            elif self.airline_area=='区域三':
                if self.cabin_type == '头等舱' or self.cabin_type == '公务舱'or self.cabin_type=='豪华头等舱':
                    count=-1
                    if self.Ticket_type == '成人票' or self.Ticket_type == '儿童票':
                        count = 2
                    else:
                        count = 0

                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1170
                        elif count == -1:
                            total_pay += 1170
                        elif count <= -2:
                            total_pay += 1590
                        if self.Baggage_list[i][4] == '否':  # 普通行李的尺寸超了
                            if (float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))>=158 and(float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))<=203:
                                total_pay+=520
                        count=count-1
                elif self.cabin_type == '超级经济舱' or self.cabin_type=='悦享经济舱':
                    count=2
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1170
                        elif count == -1:
                            total_pay += 1170
                        elif count <= -2:
                            total_pay += 1590
                        w=float(self.Baggage_list[i][0])
                        s=float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3])

                        if (w<=32 and w>23) and (s<=203 and s>158):
                            total_pay+=520
                        elif (w<=32 and w>23) or (s<=203 and s>158):
                            total_pay+=520
                        count=count-1

                else:
                    count=0#区域三 根据经济舱定义 免费额为1
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1170
                        elif count == -1:
                            total_pay += 1170
                        elif count <= -2:
                            total_pay += 1590
                        w = float(self.Baggage_list[i][0])
                        s = float(self.Baggage_list[i][1]) + float(self.Baggage_list[i][2]) + float(self.Baggage_list[i][3])
                        if (w <= 32 and w > 23) and (s <= 203 and s > 158):
                            total_pay += 520
                        elif (w <= 32 and w > 23) or (s <= 203 and s > 158):
                            total_pay += 520
                        count=count-1
            elif self.airline_area=='区域四':
                if self.cabin_type == '头等舱' or self.cabin_type == '公务舱'or self.cabin_type=='豪华头等舱':
                    count=-1
                    if self.Ticket_type == '成人票' or self.Ticket_type == '儿童票':
                        count = 2
                    else:
                        count = 0

                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1380
                        elif count == -1:
                            total_pay += 1380
                        elif count <= -2:
                            total_pay += 1590
                        if self.Baggage_list[i][4] == '否':  # 普通行李的尺寸超了
                            if (float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))>=158 and(float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))<=203:
                                total_pay+=1040
                        count=count-1
                elif self.cabin_type == '悦享经济舱' or self.cabin_type == '超级经济舱':
                    count=2
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1380
                        elif count == -1:
                            total_pay += 1380
                        elif count <= -2:
                            total_pay += 1590
                        w=float(self.Baggage_list[i][0])
                        s=float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3])
                        if self.Baggage_list[i][4] == '否':  # 一般行李
                            if w <= 23 and s <= 203 and s > 158:
                                total_pay += 1040
                            elif w <= 32 and w > 23 and s <= 203 and s > 158:
                                total_pay += 2050
                            elif w <= 32 and w > 28 and s <= 158 and s >= 60:
                                total_pay += 1040
                            elif w <= 28 and w > 23 and s <= 158 and s >= 60:
                                total_pay += 690
                        elif self.Baggage_list[i][4] == '是' and self.Baggage_list[i][6] == '是':  # 计入免费额的特殊行李
                            if w <= 32 and w > 28:
                                total_pay += 1040
                            elif w <= 28 and w > 23:
                                total_pay += 690
                        count=count-1

                else:
                    count=0#区域三 根据经济舱定义 免费额为1
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 1380
                        elif count == -1:
                            total_pay += 1380
                        elif count <= -2:
                            total_pay += 1590
                        w = float(self.Baggage_list[i][0])
                        s = float(self.Baggage_list[i][1]) + float(self.Baggage_list[i][2]) + float(
                            self.Baggage_list[i][3])
                        if self.Baggage_list[i][4] == '否':  # 一般行李
                            if w <= 23 and s <= 203 and s > 158:
                                total_pay += 1040
                            elif w <= 32 and w > 23 and s <= 203 and s > 158:
                                total_pay += 2050
                            elif w <= 32 and w > 28 and s <= 158 and s >= 60:
                                total_pay += 1040
                            elif w <= 28 and w > 23 and s <= 158 and s >= 60:
                                total_pay += 690
                        elif self.Baggage_list[i][4] == '是' and self.Baggage_list[i][6] == '是':  # 计入免费额的特殊行李
                            if w <= 32 and w > 28:
                                total_pay += 1040
                            elif w <= 28 and w > 23:
                                total_pay += 690
                        count=count-1
            elif self.airline_area=='区域五':
                if self.cabin_type == '头等舱' or self.cabin_type == '公务舱'or self.cabin_type=='豪华头等舱':
                    count=-1
                    if self.Ticket_type == '成人票' or self.Ticket_type == '儿童票':
                        count = 2
                    else:
                        count = 0

                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 830
                        elif count == -1:
                            total_pay += 1100
                        elif count<= -2:
                            total_pay += 1590
                        if self.Baggage_list[i][4] == '否':  # 普通行李的尺寸超了
                            if (float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))>=158 and(float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3]))<=203:
                                total_pay+=520
                        count=count-1
                elif self.cabin_type == '悦享经济舱' or self.cabin_type == '超级经济舱':
                    count=2
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 830
                        elif count == -1:
                            total_pay += 1100
                        elif count <= -2:
                            total_pay += 1590
                        w=float(self.Baggage_list[i][0])
                        s=float(self.Baggage_list[i][1])+float(self.Baggage_list[i][2])+float(self.Baggage_list[i][3])
                        if self.Baggage_list[i][4] == '否':  # 一般行李
                            if w <= 23 and s <= 203 and s > 158:
                                total_pay += 520
                            elif w <= 32 and w > 23 and s <= 203 and s > 158:
                                total_pay += 830
                            elif w <= 32 and w > 28 and s <= 158 and s >= 60:
                                total_pay += 520
                            elif w <= 28 and w > 23 and s <= 158 and s >= 60:
                                total_pay += 210
                        elif self.Baggage_list[i][4] == '是' and self.Baggage_list[i][6] == '是':  # 计入免费额的特殊行李
                            if w <= 32 and w > 28:
                                total_pay += 520
                            elif w <= 28 and w > 23:
                                total_pay += 210
                        count=count-1

                else:
                    count=1
                    for i in range(self.bag_num):
                        if count == 0:
                            total_pay += 830
                        elif count == -1:
                            total_pay += 1100
                        elif count <= -2:
                            total_pay += 1590
                        w = float(self.Baggage_list[i][0])
                        s = float(self.Baggage_list[i][1]) + float(self.Baggage_list[i][2]) + float(
                            self.Baggage_list[i][3])
                        if self.Baggage_list[i][4] == '否':  # 一般行李
                            if w <= 23 and s <= 203 and s > 158:
                                total_pay += 520
                            elif w <= 32 and w > 23 and s <= 203 and s > 158:
                                total_pay += 830
                            elif w <= 32 and w > 28 and s <= 158 and s >= 60:
                                total_pay += 520
                            elif w <= 28 and w > 23 and s <= 158 and s >= 60:
                                total_pay += 210
                        elif self.Baggage_list[i][4] == '是' and self.Baggage_list[i][6] == '是':  # 计入免费额的特殊行李
                            if w <= 32 and w > 28:
                                total_pay += 520
                            elif w <= 28 and w > 23:
                                total_pay += 210
                        count=count-1


        for i in range(self.bag_num):
            if self.Baggage_list[i][4]=='是'and self.Baggage_list[i][6]=='否':#不计入免费托运额的行李
                if self.Baggage_list[i][5]=='类型1':
                    total_pay+=0
                elif self.Baggage_list[i][5]=='类型3':
                    if float(self.Baggage_list[i][0])<=23 and float(self.Baggage_list[i][0])>=2:
                        total_pay+=2600
                    elif float(self.Baggage_list[i][0])<=32 and float(self.Baggage_list[i][0])>=23:
                        total_pay+=3900
                    elif float(self.Baggage_list[i][0])<=45 and float(self.Baggage_list[i][0])>=32:
                        total_pay+=5200

                elif self.Baggage_list[i][5] == '类型4':
                    if float(self.Baggage_list[i][0]) <= 23 and float(self.Baggage_list[i][0]) >= 2:
                        total_pay += 1300
                    elif float(self.Baggage_list[i][0]) <= 32 and float(self.Baggage_list[i][0]) >= 23:
                        total_pay += 2600
                    elif float(self.Baggage_list[i][0]) <= 45 and float(self.Baggage_list[i][0]) >= 32:
                        total_pay += 3900
                elif self.Baggage_list[i][5]=='类型6':
                    if float(self.Baggage_list[i][0])<=23 and float(self.Baggage_list[i][0])>=2:
                        total_pay+=490
                    elif float(self.Baggage_list[i][0])<=32 and float(self.Baggage_list[i][0])>=23:
                        total_pay+=3900
                    else:
                        total_pay=-1
                elif self.Baggage_list[i][5]=='类型7':
                    if float(self.Baggage_list[i][0])<=23 and float(self.Baggage_list[i][0])>=2:
                        total_pay+=1300
                    elif float(self.Baggage_list[i][0])<=32 and float(self.Baggage_list[i][0])>23:
                        total_pay+=2600
                    else:
                        total_pay=-1
                elif self.Baggage_list[i][5]=='类型8':
                    if float(self.Baggage_list[i][0])<=5 and float(self.Baggage_list[i][0])>=2:
                        total_pay+=1300
                    else:
                        total_pay=-1
                elif self.Baggage_list[i][5]=='类型9':
                    if float(self.Baggage_list[i][0])<=8 and float(self.Baggage_list[i][0])>=2:
                        total_pay+=3900
                    elif float(self.Baggage_list[i][0])<=23 and float(self.Baggage_list[i][0])>=8:
                        total_pay+=5200
                    elif float(self.Baggage_list[i][0])<=32 and float(self.Baggage_list[i][0])>=23:
                        total_pay+=7800
                    else:
                        total_pay=-1
        rate=0
        dw=''
        if self.start == '国内':
            rate = 1
            dw='元'
        elif self.start == '欧元区':
            rate = 7.59
            dw='欧元'
        elif self.start == '加拿大':
            rate = 4.93
            dw='加元'
        else:
            rate = 7.09
            dw='美元'
        return round(total_pay/rate),dw



















