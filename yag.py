import yagmail

receiver = "iamakashrajasingh@gmail.com"
body = "Hello there from Yagmail"
filename = "document.pdf"

yag = yagmail.SMTP("srajecebita@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)
