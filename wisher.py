import pandas as pd
import datetime
import smtplib

#your gmail credentials here
GMAIL_ID = 'your_email_here'
GMAIL_PWD = 'your_password_here'

#Function for sending email
def sendEmail(to,sub,msg):
    s = smtplib.SMTP('smtp.gmail.com',587)                          #conncection to gmail
    s.starttls()                                                    #starting the session
    s.login(GMAIL_ID,GMAIL_PWD)                                     #login using credentials
    s.sendmail(GMAIL_ID,to,f"Subject : {sub}\n\n{msg}")             #sending email
    s.quit()                                                        #quit the session
    print(f"Email sent to {to} with subject {sub} and message : {msg}")

if __name__=="__main__":
    df = pd.read_excel("BATCH 2016.xlsx")                           #read the excel sheet having all the details
    today = datetime.datetime.now().strftime("%d-%m")               #today's date in format : DD-MM
    yearNow = datetime.datetime.now().strftime("%Y")                #current year in format : YY
    writeInd = []                                                   #writeindex list

    for index,item in df.iterrows():
        msg = f"Many Many Happy Returns of the day dear {item['NAME']} !!!!!!\n\n\nThis is an automated email from Ashutosh Krishna sent using Python.\n"
        bday = item['Birthday'].strftime("%d-%m")                   #stripping the birthday in excel sheet as : DD-MM
        if (today==bday) and yearNow not in str(item['Year']):      #condition checking
            sendEmail(item['Email'], "Happy Birthday", msg)         #calling the sendEmail function
            writeInd.append(index)                                  

    for i in writeInd:
        yr = df.loc[i,'Year']
        df.loc[i,'Year'] = str(yr) + ',' + str(yearNow)             #this will record the years in which email has been sent

    df.to_excel('BATCH 2016.xlsx', index=False)                     #saving all the changes into the same excel sheet