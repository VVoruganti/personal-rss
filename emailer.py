import smtplib

smtp = smtplib.SMTP("smtp.gmail.com", 587)

# Required to setup the server
smtp.ehlo()
smtp.starttls()

user = input("Username: ")
# For Gmail this is probably an app password
pswd = input("Password: ")

# Authenticates the user
smtp.login(user, pswd)

source = input("Who is sending: ")
target = input("Who is receiving: ")

# For some reason there could not be a space between the \n and the next letter
# Could probably be better by just using triple quote messages
smtp.sendmail(source, target, 
        """Subject: So long.\n

        Dear Alice, so long and thanks for all the fish. Sincerely, Bob

        """)

# Closes the server
smtp.quit()




