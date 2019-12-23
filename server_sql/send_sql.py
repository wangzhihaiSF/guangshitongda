import pymysql
from sshtunnel import SSHTunnelForwarder
from datetime import datetime, date, timedelta
import pandas


# 由于服务器C 无法直接登录，机器B是唯一的跳转机器：可直接登录
# 通过机器B,登录机器C的MySQL,


class SendSql(object):
    def __init__(self):
        self.sever = SSHTunnelForwarder(
            ('172.18.56.18', 22),  # B机器的配置
            ssh_password='ZfpXN%URuj',
            ssh_username='isms',
            remote_bind_address=('172.18.56.25', 33071))  # C机器的配置

    def connect_mysql(self, server):
        server.start()
        db = pymysql.connect(
            host='127.0.0.1',  # 此处必须是是127.0.0.1
            port=server.local_bind_port,
            user='root',
            passwd='Zndx2018',
            db='ctcc-mcs-dispost')
        return db

    def search_data(self, db, sql):
        cur = db.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return result

    def write_data(self, result, file_name):
        # with open(file_name, "w", newline="", encoding="utf-8") as f:
        #     csv_writer = csv.writer(f)
        #     for i in data:
        #         csv_writer.writerow(i)
        df = pandas.DataFrame(data=result)
        df.to_csv(file_name, encoding="utf-8", header=False, index=False)


if __name__ == '__main__':
    yesterday = date.today() + timedelta(days=-1)
    today = date.today() + timedelta(days=1)
    data_search = SendSql()
    db = data_search.connect_mysql(data_search.sever)
    # 厂商打点数据
    sql1 = 'select phone_manufacturers, type, count(*) from statistics_common where mobile_time >= "%s" and mobile_time < "%s" group by phone_manufacturers, type' %(yesterday, today)
    # 各个厂商日活
    sql2 = 'select a.phone_manufacturers , count(*) from (select phone_manufacturers,imei from statistics_common where create_time >= "%s" and create_time < "%s" group by phone_manufacturers, imei) as a group by a.phone_manufacturers' %(yesterday, today)
    # 手机终端量查询
    sql3 = 'select a.phone_manufacturers, count(*) from (select phone_manufacturers , imei from statistics_common where mobile_time < "%s" group by phone_manufacturers, imei) as a group by a.phone_manufacturers' % today
    # 号码短信量
    sql4 = 'select sms_number, count(*) from new_message_statistics where create_time >= "%s" and create_time < "%s" group by sms_number order by numbers desc limit 100' % (yesterday, today)
    sql_list = [sql3, sql4]
    files = ["日厂商打点数据.csv", "各个厂商日活.csv", "手机终端量.csv", "号码短信量.csv"]
    for i in range(len(sql_list)):
        n = i + 1
        print("第 %s 条语句执行中：%s" % (n, datetime.now()))
        data = data_search.search_data(db, sql_list[i])
        print("查询结束，开始写入文件")
        data_search.write_data(data, files[i])
    data_search.sever.close()
