import requests
import time

class LookUp:
    def __init__(self, uid):
        self.id = 0
        self.url = "https://api.twitter.com/2/users/{}/tweets".format(uid)
        with open("secrets.txt", "r") as file:
            self.secret = file.read()

    def get_tweets(self):
        headers = {"Authorization": "Bearer {}".format(self.secret)}
        data = requests.get(self.url, headers=headers)
        if data.status_code != 200:
            raise Exception("Request returned an error: {} {}".format(data.status_code, data.text))

        return data.json()

    def makepretty(self, data):
        if (self.id != data['meta']['newest_id']):
            for i in data['data']:
                print("Elon: {}, https://twitter.com/elonmusk/status/{} \n".format(i['text'], i['id']))
            print("tweets: {}".format(data['meta']['result_count']))        
        
        self.id = data['meta']['newest_id']


def main():
    print("<WhatsUpElon>  Copyright (C) <2021>  <kupr744>\nThis program comes with ABSOLUTELY NO WARRANTY;\n\
This is free software, and you are welcome to redistribute it\nunder certain conditions;\n")

    x = LookUp(44196397)

    while(True):
        data = x.get_tweets()
        x.makepretty(data)
        time.sleep(60 * 5)

if __name__ == "__main__":
    main()