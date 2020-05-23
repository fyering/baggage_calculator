import xlrd
class ExcelUtil(object):
    def __init__(self,excelPath,sheetname):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetname)
        # get titles
        self.row = self.table.row_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1

    def next(self):
        l=[]
        while self.hasNext():
            s={}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            self.curRowNo += 1
            l.append(s)
        return l

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True
