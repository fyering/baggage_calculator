import HTMLTestRunner
import unittest
from TestCase import TestClass

if __name__=='__main__':
    suite=unittest.makeSuite(TestClass)
    filename='D:\\myreport.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(fp,title=u'my unit test',description=u'This is a report test')
    runner.run(suite)