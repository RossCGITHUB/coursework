# package for email services 
import smtplib
import string
TO = "1507073@rgu.ac.uk"
FROM = "RASPPI@ROSSdomain.com"
SUBJECT = "Temperature is too high!!"
text = "The temperature on your Raspberry Pi is running dangerously high, please check the webserver for more details! "

BODY = string.join(("From: %s" %FROM,"To: %s" %TO,"Subject: %s" %SUBJECT, "",text), "\r\n")
server = smtplib.SMTP('127.0.0.1', 1025)
server.sendmail(FROM, [TO], BODY)
server.quit()