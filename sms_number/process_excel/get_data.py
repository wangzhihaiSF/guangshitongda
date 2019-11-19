from sms_number.process_excel import operation_excel, data_config


class GetData:
    def __init__(self):
        self.opera_excel = operation_excel.OperationExcel()

    # 获取个数
    def get_case_lines(self):
        rows = self.opera_excel.get_lines()
        return rows

    # 写organization数据
    def write_organization_result(self, row, value):
        col1 = data_config.get_organization()
        self.opera_excel.write_value(row, col1, value)

    # 写business
    def write_business_result(self, row, value):
        col2 = data_config.get_business()
        self.opera_excel.write_value(row, col2, value)


if __name__ == "__main__":
    get_data = GetData()
    lines = get_data.get_case_lines()
    get_data.write_result(1, "ss")
    print(lines)
