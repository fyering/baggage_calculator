import sys
import unittest,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)
import HTMLTestRunner
import unittest
from Test.test import DataTest
import sys
if __name__=='__main__':
    suite=unittest.makeSuite(DataTest)
    filename='C:\\Program Files (x86)\\Jenkins\\workspace\\python_test\\test_report\\'+sys.argv[1]+".html"

    fp=open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'my unit test', description=u'This is a report test')
    runner.run(suite)