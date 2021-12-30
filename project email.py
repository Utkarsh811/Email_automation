import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




def email(username):
    fromaddr= "user email "
    password= "password"
    toaddr=username

    #instance of mimemultipart

    msg = MIMEMultipart()

    # storing recepient and sender email addres
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject']= " AUTO GENERATED MAIL BY AGENT-P"

    # STRING TO STORE THE BODY OF THE MAIL
    body= " HAPPY CHRISTMAS AND NEW YEAR TO YOU . this is an auto generated mail for a testing purpose. Apologies for inconvenience. Please dont reply to this email"

    # attach the body with the instance
    msg.attach(MIMEText(body,'plain'))

    #open the file to be sent

    filename= "happynewyear.png"
    attachment = open(filename,"rb")


    #instance of mimebase and named as p
    p= MIMEBase('application' , 'octet-stream')

    #to change the payload into the encoded form

    p.set_payload((attachment).read())



    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition',  "attachment; filename=%s" %filename)

    msg.attach(p)


    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr,password)

    #convert the multipart msg into a string

    text =msg.as_string()
    server.send_message(msg)


    server.quit()
    
if(__name__=="__main__"):
    
   
    list=["recipient mail"," recepient mail" ]
    
    for i in range(len(list)):
      
        email(list[i])
      