# coding=utf-8
import sys
import unittest,os
from ddt import ddt,data,unpack
from Test.ExcelUtil import ExcelUtil
from BaggageCalculator.Calculator import Calculator
from BaggageCalculator.Package import package
from BaggageCalculator.SpecialPackage import SpecialPackage
from BaggageCalculator.Ticket import Ticket
import HTMLTestRunner

excel = ExcelUtil("D:\\Course\\Lab1\\Lab1\\Testcase\\TEST.xlsx", '黑盒测试')
@ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('stop')

    @data(*excel.next())
    def testCalculator(self, data):
        packages=[]
        specialpackages=[]
        t=None
        if '重量' in data and '长' in data and '宽'in data and '高' in data:
            string_weight=str(data['重量'])
            weights=string_weight.split('+')
            for item in weights:
                p = package(float(data['长']), float(data['宽']), float(data['高']), float(item))
                packages.append(p)
        if 'weight' in data and 'Type' in data:
            string_special_weight = str(data['weight'])
            weights_special = string_special_weight.split('+')
            for item in weights_special:
                s = SpecialPackage(float(item), data['Type'])
                specialpackages.append(s)
        if '座舱类型' in data and '乘客类型' in data and '票价' in data and 'Area' in data and 'Card' in data:
            t=Ticket(data['座舱类型'], data['乘客类型'], float(data['票价']), data['Area'],data['Card'])
        calculate=Calculator(t,packages,specialpackages)
        IsOverweight, IsOversize, IsOutOfSize, expense = calculate.calculate()
        if '费用' in data:
            self.assertEqual(expense,float(data['费用']))
if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    # HTMLTestRunner运行
    fp=open("./test.html",'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试结果：')
    runner.run(suite)
    fp.close()
    # TextTestRunner运行
    # with open("./test.txt", "w", encoding="utf-8") as file:  # 利用上下文管理器把测试结果写入到xxx.txt中
    #     runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    #     runner.run(suite)  # 执行测试套件里面的所有用例


