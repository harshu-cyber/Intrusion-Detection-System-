from twilio.rest import Client

account_sid = 'ACd7396bd98041c33369dbeeba5b016c6c'
auth_token = '7f0b24361f6766b3ee37a7aa2813f90a'
client = Client(account_sid, auth_token)

def sendSms():
    try:
        message = client.messages.create(
            from_='+18786453317',
            body='alert',
            to='+919580951150'  
        )
        print("Message SID:", message.sid)
    except Exception as e:
        print("Error:", e)

sendSms()
