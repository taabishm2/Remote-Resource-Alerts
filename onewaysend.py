from twilio.rest import Client

def twilioSend(msg):
    account_sid = 'ACdd148d93acf8b287fd1032c96ca00d52'
    auth_token = 'aedf2fd5ceb520f5ec58787c08c559af'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body=msg,
                                  to='whatsapp:+918082575083'
                              )

