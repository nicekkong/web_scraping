import smtplib
from email.mime.text import MIMEText

# msg = MIMEText("이메일 본문입니다")
#
#
# msg['Subject'] = "이메일 발송 테스트"
# msg['from'] = 'nicekkong@naver.com'
# msg['to'] = 'nicekkong@gmail.com'
#
# s = smtplib.SMTP("smtp.gmail.com", 587)
# s.send_message(msg)
# s.quit()




def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except Exception as e:
        print("failed to send mail" + e)

send_email('nicekkong.com@gmail.com', '*******************', 'nicekkong@gmail.com', 'Title by python', 'Nice to meet you~!!')


