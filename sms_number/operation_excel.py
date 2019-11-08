import xlrd
from xlutils.copy import copy


class OperationExcel(object):
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "messages.xlsx"
            self.sheet_id = 0
        self.read_data = xlrd.open_workbook(self.file_name)
        self.write_data = copy(self.read_data)  # 复制一份，作为测试结果
        self.data = self.get_data()

    # 获取 sheet 内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]
        return table

    # 获取 table 的行数
    def get_lines(self):
        table = self.data
        return table.nrows

    # 获取单元格的值
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        sheet_data = self.write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        # 保存文件可能需要优化，虽然现在改为复制了一份，但每一次写入数据后都执行了一次保存文件
        # 只需要最后一次写入后再保存
        self.write_data.save("result.xls")


if __name__ == "__main__":
    opers = OperationExcel()
    lines = opers.get_lines()
    opers.write_data(1, 11, "ss")
    print(lines)
