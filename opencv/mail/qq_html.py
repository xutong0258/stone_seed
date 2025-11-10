import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


    # 创建HTML内容
html = """
<html>
  <head></head>
  <body>
    <p>亲爱的用户，</p>
    <p>这是使用Python发送的HTML格式邮件的示例。</p>
    <p>希望您喜欢！</p>
  </body>
</html>
"""
    

def send_QQ_email_plain():
    sender = user = '153194831@qq.com'    # 发送方的邮箱账号
    passwd = 'hfoqkzpousxwbgbf'            # 授权码
 
    receiver = '153194831@qq.com'        # 接收方的邮箱账号，不一定是QQ邮箱
 
    # 纯文本内容 
        # 将HTML内容转换为MIMEText对象
    html_part = MIMEText(html, 'html')
        # 将HTML内容添加到邮件对象中
    
    # msg = MIMEText(f'Python 邮件发送测试 {time.time()}', 'plain', 'utf-8')
    
    # 添加附件
    filename = "note.txt"  # 附件文件名
    attachment = open(filename, "rb")  # 打开附件文件
    
    msg = MIMEMultipart('alternative')
 
    # From 的内容是有要求的，前面的abc为自己定义的 nickname，如果是ASCII格式，则可以直接写
    msg['From'] = f'abc <153194831@qq.com>' 
    msg['To'] = receiver
    msg['Subject'] = 'Python SMTP 邮件测试'         # 点开详情后的标题
    
    msg.attach(html_part)
    
    try:
        # 建立 SMTP 、SSL 的连接，连接发送方的邮箱服务器
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
 
        # 登录发送方的邮箱账号
        smtp.login(user, passwd)
 
        # 发送邮件 发送方，接收方，发送的内容
        smtp.sendmail(sender, receiver, msg.as_string())
 
        print('邮件发送成功')
 
        smtp.quit()
    except Exception as e:
        print(e)
        print('发送邮件失败')

if __name__ == '__main__':
   send_QQ_email_plain()