#Step 1: go to your gmail account and set up 2 factor authentication
    #Go to google account settings > Security > 2-Step Verification
#Step 2: generate app password 
    #Go to google account settings > Security > 2-Step Verification > App Passwords
    # Type in a name for the app and click create
#Step 3: create a function for sending email:

from email.message import EmailMessage
#from password import password #importing password from another file
import ssl
import smtplib

sender = "djack737@gmail.com"
email_password = "This will be the password generated from the app password. I will not enter it her for security reasons."

receiver = "djack.737@gmail.com"

subject = "Test Email"
body = """This is a test email"""

em = EmailMessage() #creates instace of EmailMessage
em['From']= sender
em['To'] = receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, email_password)
    smtp.sendmail(sender, receiver, em.as_string())