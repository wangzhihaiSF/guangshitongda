import re
import csv


class HandleLog:
    def __init__(self):
        self.file_path = "real_log.log"
        self.sms_dict = {}

    def get_result(self):
        with open(self.file_path, "r", encoding="utf-8") as fp:
            for line in fp:
                result = self.process_data(line)
                self.write_data(result)

    def process_data(self, line):
        sms_num = self.find_sms_num(line)
        keys = self.sms_dict.keys()

        if not self.is_contain(sms_num, keys):
            self.sms_dict[sms_num] = 0
        else:
            self.sms_dict[sms_num] += 1
        return sms_num, self.sms_dict[sms_num].value

    def find_sms_num(self, line):
        sms_num_regex = re.compile('"smsNumber":".*?"')
        sms_num_result = sms_num_regex.search(line)
        if sms_num_result is not None:
            result = sms_num_result.group(1)
            return result

    def is_contain(self, str_1, array):
        if str_1 in array:
            return True
        else:
            return False

    def write_data(self, data):
        with open("messages_result.csv", "a", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(data)


if __name__ == "__main__":
    hand_log = HandleLog()
    hand_log.get_result()
