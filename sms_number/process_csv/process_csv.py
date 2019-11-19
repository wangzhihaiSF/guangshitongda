import csv
import json


class Auto_File(object):
    def __init__(self):
        self.file = r"C:\Users\DELL\Desktop\statement\messages1118.csv"
        self.save_file_name = "messages.csv"

    def load_json(self):
        with open("sms_num.json", 'r', encoding="utf-8") as f:
            json_dict = json.load(f)
        return json_dict

    def read_csv(self):
        nums_list = []
        with open(self.file, "r", encoding="utf-8") as fp:
            for line in fp:
                nums_list.append(line.split("	"))
        return nums_list

    def write_data(self, data):
        file_name = self.save_file_name
        with open(file_name, "a", encoding="utf-8-sig", newline="") as fp:
            writer = csv.writer(fp)
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
        for line in num_list:
            if len(line) > 2:
                line[3] = line[3][:-1]
            else:
                line.insert(1, "")
                line.insert(2, "")
                line[3] = line[3][:-1]
            print(line)

            self.write_data(line)


if __name__ == "__main__":
    auto = Auto_File()
    auto.my_main()
