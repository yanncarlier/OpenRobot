import requests
import json

# url = "https://openlab.openbankproject.com/obp/v3.0.0/banks/hsbc.01.hk.hsbc/accounts/f751de0f-18dd-46dc-8b36-5f9664cf0431/owner/account/"

API_V = "v3.1.0/"
BANK_ID = "hsbc.01.hk.hsbc/"
ACCOUNT_ID = "f751de0f-18dd-46dc-8b36-5f9664cf0431/"
VIEW_ID = "owner"

#/obp/v3.1.0/banks/BANK_ID/accounts/ACCOUNT_ID/VIEW_ID/funds-available
#url = "https://openlab.openbankproject.com/obp/" + API_V + "banks/" + BANK_ID + "accounts/" + ACCOUNT_ID + VIEW_ID + "/funds-available"

AMOUNT = '100000000'
CURRENCY = 'EUR'
VALIDATE = 'funds-available'

url = 'https://openlab.openbankproject.com/obp/v3.1.0/banks/hsbc.01.hk.hsbc/accounts/123/_third_party_app/' + VALIDATE + '?amount=' + AMOUNT +'&currency=' + CURRENCY

payload = ""


headers = {
    'Authorization': 'DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.VgxxO2PSSz76Vgq6tIMMS2MeRftaKxxPHd1sN2aFqHI"',
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "98e81d93-da8c-436b-a477-3f97b174553c"
    }

response = requests.request("GET", url, data=payload, headers=headers)

ANSWER = response.text[11]
#print(ANSWER)


if (ANSWER == "n"):
    print(response.text)


# a = response.text

# print(json.dumps(a, indent=2))
#print (json.dumps(a, indent=2))

# {"id":"f751de0f-18dd-46dc-8b36-5f9664cf0431","bank_id":"hsbc.01.hk.hsbc","label":"Robert.Hk.01 M35 13..280","number":"13078786280","owners":[{"id":"Robert.Hk.01","provider":"https://openlab.openbankproject.com","display_name":"Robert.Hk.01"}],"type":"CURRENT PLUS","balance":{"currency":"HKD","amount":"6544.33"},"account_routings":[{"scheme":"OBP","address":"f751de0f-18dd-46dc-8b36-5f9664cf0431"}],"account_rules":[]}
# {"id":"f751de0f-18dd-46dc-8b36-5f9664cf0431","bank_id":"hsbc.01.hk.hsbc","label":"Robert.Hk.01 M35 13..280","number":"13078786280","owners":[{"id":"Robert.Hk.01","provider":"https://openlab.openbankproject.com","display_name":"Robert.Hk.01"}],"type":"CURRENT PLUS","balance":{"currency":"HKD","amount":"6544.33"},"account_routings":[{"scheme":"OBP","address":"f751de0f-18dd-46dc-8b36-5f9664cf0431"}],"account_rules":[]}