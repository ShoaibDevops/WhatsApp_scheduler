from twilio.rest import Client

account_sid = 'AC7677f284cd559ed268f7a0c8448c5313'
auth_token = '3fdb36ab15ebbd8cd71e3f65f73def4e'
client = Client(account_sid, auth_token)

def love () :
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello,This message for testing purpose !!! by shoaib',
        to='whatsapp:+917387707069'
        #to='whatsapp:+917709075459'
        #to='whatsapp:+918237552223'
        )

        print(message.sid)