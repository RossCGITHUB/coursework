# package for email services 
import smtplib
import string
TO = "1507073@rgu.ac.uk"
FROM = "RASPPI@ROSSdomain.com"
SUBJECT = "WEB ALERT!!"
text = "The connection to www.google.com on your Raspberry Pi has dropped, please check the webserver for more details! "

BODY = string.join(("From: %s" %FROM,"To: %s" %TO,"Subject: %s" %SUBJECT, "",text), "\r\n")
server = smtplib.SMTP('127.0.0.1', 1025)
server.sendmail(FROM, [TO], BODY)
server.quit()