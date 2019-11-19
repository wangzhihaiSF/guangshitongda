from sms_number.process_excel.get_data import GetData
from sms_number.process_excel.operation_excel import OperationExcel


class RunTest:
    def __init__(self):
        self.data = GetData()
        self.message = OperationExcel()

    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):  # i 是行
            number1 = self.message.get_cell_value(i, 4)
            organization = self.message.get_cell_value(i, 5)
            business = self.message.get_cell_value(i, 6)
            for j in range(1, rows_count):  # j 是列
                number2 = self.message.get_cell_value(j, 0)
                if number1 == number2:
                    self.data.write_organization_result(j, organization)
                    self.data.write_business_result(j, business)


if __name__ == "__main__":
    run = RunTest()
    run.go_on_run()
