from unittest import TestCase
from rule import rule

class TestRule(TestCase):
    def setUp(self):
        self.airline_area = '国内'
        self.start = '国内'
        self.cabin_type = '公务舱'
        self.Ticket_type = '成人票'
        self.price = '1111'
        self.Baggage_list = ['重量:30 长:30 宽:30 高:30 特殊行李:否 类型:无 免费额:无']























    def test_case24(self):
        self.airline_area = '国内'
        self.start = '国内'
        self.cabin_type = '经济舱'
        self.Ticket_type = '成人票'
        self.price = '1111'
        self.Baggage_list = ['重量:30 长:30 宽:30 高:140 特殊行李:是 类型:类型1 免费额:否']

        r = rule(self.Baggage_list, self.airline_area, self.start, self.cabin_type, self.Ticket_type, self.price)
        result, dw = r.count_dollar()
        self.assertEqual(result, round(980))




