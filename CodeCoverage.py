# coding=utf8
import os
import time




def codeCoverage():
    now = time.strftime("%Y%m%d%H%M")
    htmlReport = os.getcwd() + "\\" + "CoverageReport"
    htmlCmd = "coverage html -d  " + htmlReport + "\\" + now
    runPyCmd = "coverage run " + "TestCase.py"
    if os.path.exists(htmlReport):
        os.system(runPyCmd)
        os.system(htmlCmd)
    else:
        os.mkdir(htmlReport)
        os.system(runPyCmd)
        os.system(htmlCmd)


if __name__ == "__main__":
    codeCoverage()