import requests

class LookUp:

    def __init__(self, uid):
        self.keywords = []
        self.count = 100
        self.url = "https://api.twitter.com/2/users/{}/tweets".format(uid)
        
        with open("secrets.txt", "r") as file:
            self.secret = file.read()
        
        try:
            with open("keywords.txt", "r") as file:
                for line in file:
                    if line[0] == '#':
                        continue
                    self.keywords.append(line)

                if len(self.keywords) == 0:
                    raise RuntimeError('no keywords')
        except RuntimeError as err:
            print("caught error: " + repr(err))
            self.count = 15

        if len(self.keywords) != 0:
            print("Keywords: {}\n".format(self.keywords))

    def get_tweets(self):
        headers = {"Authorization": "Bearer {}".format(self.secret)}
        params = {"max_results" : "{}".format(self.count)}

        data = requests.get(self.url, headers=headers, params=params)
        if data.status_code != 200:
            raise Exception("Request returned an error: {} {}".format(data.status_code, data.text))
        return data.json()

    def makepretty(self, data) -> None:
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
    

def main() -> None:
    print('''<WhatsUpElon>  Copyright (C) <2021>  <kupr744>\nThis program comes with ABSOLUTELY NO WARRANTY;\n\This is free software, and you are welcome to redistribute it\nunder certain conditions;\n''')

    x = LookUp(44196397)

    data = x.get_tweets()
    x.makepretty(data)
        

if __name__ == "__main__":
    main()
