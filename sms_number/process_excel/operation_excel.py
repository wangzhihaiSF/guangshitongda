import json

import xlrd
from xlutils.copy import copy


class OperationExcel(object):
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = r"C:\Users\DELL\Downloads\20191129.1520.xlsx"
            # self.file_name = "messages.xlsx"
            self.sheet_id = 0
        self.read_data = xlrd.open_workbook(self.file_name)
        self.write_data = copy(self.read_data)  # 复制一份，作为测试结果
        self.data = self.get_data()
        self.rows = self.get_lines()
        self.dict = {}

    # 获取 sheet 内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]
        return table

    # 将数据生成字典
    def create_dic(self):
        for i in range(1, self.rows):
            sms_num = int(self.get_cell_value(i, 1))
            organization = self.get_cell_value(i, 2)
            business = self.get_cell_value(i, 3)
            self.dict[sms_num] = (organization, business)

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
        self.write_data.save("result.xls")

    # 将字典写入json
    def write_json(self, dict):
        json_str = json.dumps(dict, ensure_ascii=False, indent=4)
        with open('sms_num.json', 'w', encoding="utf-8") as json_file:
            json_file.write(json_str)


if __name__ == "__main__":
    opers = OperationExcel()
    opers.create_dic()
    # 在将excel的数据转化成json文件时，excel中的数据必须是文本，避免长数字显示不全
    opers.write_json(opers.dict)



