import smtplib
import getpass


smtpobject=smtplib.SMTP('smtp.gmail.com',587)

smtpobject.ehlo()

smtpobject.starttls()


email = getpass.getpass('Email please')
password = getpass.getpass('Password please')


smtpobject.login(email, password)

from_address = email
to_address = email

subject_line= "my subject"

message = "my email body"

msg = "Subject: "+subject_line+'\n'+message

smtpobject.sendmail(from_address,to_address)

