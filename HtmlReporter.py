import HTMLTestRunner
import unittest
from TestCase import TestClass
import sys
if __name__=='__main__':
    suite=unittest.makeSuite(TestClass)
    filename='C:\\Program Files (x86)\\Jenkins\\workspace\\python_test\\test_report\\'+sys.argv[1]+".html"

    fp=open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'my unit test', description=u'This is a report test')
    runner.run(suite)