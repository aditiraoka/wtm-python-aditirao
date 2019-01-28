import smtplib

sender='harry.potter@gmail.com'
reciever=['you@gmail.com.com']

message="""From:  Harry Potter <harry.potter@gmail.com>
To: You <you@gmail.com>
Subject: DA meeting

This is to inform you about the next Dumbledore's Army meeting, which is tomorrow in RoR.
Attend without fail.
Regards,
Harry J P
"""

try:
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtpObj.login('harry.potter','******')
    smtpObj.sendmail(sender,reciever,message)
    print ("Sucess !")
except SMTPException:
    print ("Error !")
