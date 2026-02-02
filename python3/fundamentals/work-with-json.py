import json
import datetime

jsonPerson = '{ "firstName": "Mehdi", "lastName": "Karimi", "birthday": "1982-11-28" }'

person = json.loads(jsonPerson)
print(person["firstName"])

order = {
    "traderId": "123456789",
    "userId": 3654,
    "instrumentId": "IROLAB123456",
    "quantity": 1500,
    "price": 2650,
    "entryDate": str(datetime.datetime.now())
}
jsonOrder = json.dumps(order, indent= 4)

print(jsonOrder)