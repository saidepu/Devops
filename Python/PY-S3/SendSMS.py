from twilio.rest import Client

account_sid = 'AC3593025b5164088a1d7139d73143034d'
auth_token = 'f446949ef20b337924e5acabb671a688'

myPhone = '+917299095445'
TwilioNumber = '+19497991485'

client = Client(account_sid,auth_token)

client.messages.create(to=myPhone, from_=TwilioNumber, body= 'I have sent a text message from python!')