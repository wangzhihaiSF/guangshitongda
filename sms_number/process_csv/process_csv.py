import csv
import json
import os


class AutoFile(object):
    def __init__(self):
        self.read_file = r"C:\Users\DELL\Desktop\statement\weekmessages1206.csv"
        self.save_file_name = r"D:\PycharmProjects\guangshitongda\sms_number\process_csv\messages.csv"

    def load_json(self):
        with open("sms_num.json", 'r', encoding="utf-8") as f:
            json_dict = json.load(f)
        return json_dict

    def read_csv(self):
        nums_list = []
        try:
            with open(self.read_file, "r", encoding="utf-8") as fp:
                for line in fp:
                    nums_list.append(line.split("	"))
            return nums_list
        except FileNotFoundError:
            print("文件不存在")
            return nums_list

    def is_exists(self):
        if os.path.exists(self.save_file_name):
            # 删除文件,path为文件路径
            os.remove(self.save_file_name)

    def write_data(self, data):
        file_name = self.save_file_name
        with open(file_name, "a", encoding="utf-8-sig", newline="") as fp:
            writer = csv.writer(fp, delimiter="	")
            writer.writerow(data)

    def process(self):
        nums_list = self.read_csv()
        json_dict = self.load_json()
        for key in json_dict.keys():
            for j in nums_list:
                if key == j[0]:
                    j.insert(1, json_dict[key][0])
                    j.insert(2, json_dict[key][1])
        return nums_list

    def my_main(self):
        num_list = self.process()
        if num_list:
            for line in num_list:
                if len(line) > 2:
                    line[3] = line[3][:-1]
                else:
                    line.insert(1, "")
                    line.insert(2, "")
                    line[3] = line[3][:-1]
                self.write_data(line)
        else:
            print("停止运行！")


if __name__ == "__main__":
    auto = AutoFile()
    auto.is_exists()
    auto.my_main()
