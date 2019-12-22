import smtplib 
  
# list of email_id to send the mail 
li = ["iamakashrajasingh@gmail.com", "srajece@gmail.com"] 
  
for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("srajecebita@gmail.com", "rajkumar1987") 
    message = "Message_you_need_to_send"
    s.sendmail("srajecebita@gmail.com", li[i], message) 
    s.quit()
