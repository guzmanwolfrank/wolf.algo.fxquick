#you can get both your DEMO or Live API Key at Oanda in the API page. 

API_KEY = "PLACE YOUR API KEY HERE"
ACCOUNT_ID = "PLACE YOUR ACCOUNT NUMBER ID HERE"


# Make sure to use Demo Live server, you only need prices which are live, 
# not a transaction. 
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'

#Secure Header 

SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}'
}

print(OANDA_URL)
