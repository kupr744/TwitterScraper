from typing import List
import requests
import time

class LookUp:

    def __init__(self, uid):
        self.keywords = []
        self.url = "https://api.twitter.com/2/users/{}/tweets".format(uid)
        
        with open("secrets.txt", "r") as file:
            self.secret = file.read()
        try:
            with open("keywords.txt", "r") as file:
                for line in file:
                    self.keywords.append(line.splitlines()[0])
        except:
            print("no keywords, huh?\n")

        if( len(self.keywords) != 0):
            print("Keywords: {}\n".format(self.keywords))

    def get_tweets(self):
        headers = {"Authorization": "Bearer {}".format(self.secret)}
        params = {"max_results" : "100"}

        data = requests.get(self.url, headers=headers, params=params)
        if data.status_code != 200:
            raise Exception("Request returned an error: {} {}".format(data.status_code, data.text))
        return data.json()

    def makepretty(self, data):
        counter = 0
        
        if(len(self.keywords) == 0):
            for i in data['data']:
                print("Elon: {}, https://twitter.com/elonmusk/status/{} \n".format(i['text'], i['id']))   
                counter += 1     
        else:
            for i in data['data']:
                for key in self.keywords:
                    if key in i['text']:
                        print("Elon: {}, https://twitter.com/elonmusk/status/{} \n".format(i['text'], i['id']))
                        #continue
                        counter += 1 
        
        print("found {} tweets".format(counter))
    

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