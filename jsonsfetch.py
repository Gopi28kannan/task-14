import requests
class jsonss:
    def __init__(self, web_url):
        self.url = web_url

    #fetch data
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    #display the country names, currency name  and currency symbols
    def name(self):
        list3=[]
        m='currencies';p='symbol'
        print('country names and currencies name and currency symbols')
        for data in self.fetch_data():
            print('country name:',data['name']['official'])
            if m in data:
                for k,v in data[m].items():
                    print('currency name: ', v['name'])
                    if p in data[m][k]:
                        print('currency symbol: ',v[p])
                    else:
                        print('currency symbol:  none') 
            else:
                print('null')
            print()

     #display all those countries which have dollar as its currency       
    def dollar_name(self):
         list1 = []
         print("\n\n\ncountry which have dollar as its currency")
         for data1 in self.fetch_data():
             currency_keys = list(data1.get('currencies', {}).keys())
             if currency_keys == ["USD"]:
                 # print(name)
                 # print(currency_keys)
                 list1.append(data1['name']['common'])
         for i in list1:
             print(i)

     #display all those countries which have euro as its currency
    def euro_name(self):
        list2 = []
        print('\n\n\n')
        print("country which have euro as its currency")
        for data2 in self.fetch_data():
            name = data2["name"]["common"]
            currency_keys = list(data2.get('currencies', {}).keys())
            if currency_keys == ["EUR"]:
                # print(name)
                # print(currency_keys)
                list2.append(data2["name"]["common"])
        for i in list2:
            print(i)

url = "https://restcountries.com/v3.1/all"
s = jsonss(url)
s.name()
s.dollar_name()
s.euro_name()

