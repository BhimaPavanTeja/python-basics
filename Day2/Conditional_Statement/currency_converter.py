amount = 100
currency = 'USD'
rates = {'USD': 74.5, 'EUR': 89.7, 'INR': 1}
if currency in rates:
    print(amount * rates[currency])
else:
    print("Invalid currency")