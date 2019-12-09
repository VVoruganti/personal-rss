import imapclient, pyzmail

# Key for different providers
# gmail : imap.gmail.com
# outlook : imap-mail.outlook.com
imap = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')

imap.select_folder('INBOX', readonly=True)

UIDs = imap.search(['SINCE 05-Jul-2014'])
  
rawMessages = imap.fetch(UIDs, 'BODY[]', 'FLAGS')

print(rawMessages)

imap.logout()
