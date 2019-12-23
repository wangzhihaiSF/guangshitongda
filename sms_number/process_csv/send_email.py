import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendEmail(object):
    def __init__(self):
        self.server = smtplib.SMTP("smtp.qq.com")
        self.from_email = "1599315665@qq.com"
        # 需要授权码
        self.email_password = ""
        self.to_email = ["wangzhihai@unioncast.cn"]

    def email_content(self):
        # 邮件正文
        content = "脚本发送邮件测试"
        # 实例化一个MIMEText邮件对象，三个参数，分别是邮件正文，文本格式和编码.
        message = MIMEText(content, "plain", "utf-8")
        # 主题
        subject = "日报表"
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = self.from_email
        # 接受方信息
        message['To'] = self.to_email[0]
        try:
            server = smtplib.SMTP('smtp.163.com')  # 163邮箱服务器地址，端口默认为25
            server.login(self.from_email, self.email_password)
            server.sendmail(self.from_email, self.to_email, message.as_string())
            print('success')
            server.quit()

        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误



