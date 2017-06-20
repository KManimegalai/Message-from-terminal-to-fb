import smtplib

li = ["tamil1994civil@gmail.com", "emownika@gmail.com","ajitha24397@gmail.com","srianuradha8@gmail.com"]
email=str(raw_input("your emailid: "))

for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, '7639108959')
    message = "May 26 is celebrated as the Science Day in Switzerland in honour of former President Dr. APJ Abdul Kalam, because on the day, Kalam visited the country :)"
    
    s.sendmail(email, li[i], message)
    s.quit()
print("Email is sent sucessfully")
