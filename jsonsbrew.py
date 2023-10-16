import requests
class Brew:
    def __init__(self, web_url, state):
        self.url = web_url
        self.stat = state

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    def details_of_brewaries(self,state):
        counts = {}
        count1 = 0
        self.stat = state
        for data in self.fetch_data():
            if str(data['state']) == self.stat:
                print(data['name'])
                count1 = count1 + 1
        print("Number of Breweries ", count1)

    def type_brew(self,state):
        self.stat = state
        list1 = []
        res1 = {}
        for data in self.fetch_data():
            list1.append(data['brewery_type'])
            for i in list1:
                res1[i] = list1.count(i)
        print(res1)

    def count_web_brew(self,state):
        self.state= state
        count2 = 0
        for data in self.fetch_data():
            if data['website_url']:
                print(data['website_url'])
                count2 = count2 + 1
        print("number of breweries having websites in the state", self.state, "is", count2)

url1 = "https://api.openbrewerydb.org/v1/breweries?by_state=Alaska"
url2 = "https://api.openbrewerydb.org/v1/breweries?by_state=Maine"
url3 = "https://api.openbrewerydb.org/v1/breweries?by_state=New%20York"
s = Brew(url1, "Alaska")
s1 = Brew(url2,"Maine")
s2 = Brew(url3, "New York")
print("All breweries present in Alaska\n")
s.details_of_brewaries("Alaska")
print('----------------------------------------------------------\n\n')
print("All breweries present in Maine\n")
s1.details_of_brewaries("Maine")
print('----------------------------------------------------------\n\n')
print("All breweries present in New York\n")
s2.details_of_brewaries("New York")
print('----------------------------------------------------------\n\n')
print("Alaska")
s.type_brew("Alaska")
print("Manie")
s1.type_brew("Maine")
print("New York")
s2.type_brew("New York")
print('----------------------------------------------------------\n\n')
print("breweries have websites in Alaska\n")
s.count_web_brew("Alaska")
print('----------------------------------------------------------\n\n')
print("breweries have websites in Manie\n")
s1.count_web_brew("Maine")
print('----------------------------------------------------------\n\n')
print("breweries have websites in New York\n")
s2.count_web_brew("New York")
