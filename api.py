url = 'https://www.alphavantage.co/query?function=WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=2R52NNTGYAJTUAM3'
r = requests.get(url)
data = r.json()

print(data)

to_symbol=USD
url = 'https://www.alphavantage.co/query?to_symbol=USD&from_symbol=EUR&to_symbol=USD&apikey=2R52NNTGYAJTUAM3'
r = requests.get(url)
data = r.json()
