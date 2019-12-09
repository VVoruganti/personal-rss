import smtplib

smtp = smtplib.SMTP("smtp.gmail.com", 587)

smtp.ehlo()

smtp.starttls()

user = input("Username: ")
pswd = input("Password: ")

smtp.login(user, pswd)

smtp.sendmail("MY_EMAIL_ADDRESS", "recipient_email_address", "Subject: So long.\n body of the mssage")

smtp.quit()




