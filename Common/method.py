import requests


class SendMain:
    def __init__(self, url, method, headers, payload=None):  # initialize
        self.url = url
        self.method = method
        self.headers = headers
        self.payload = payload
        self.req = self.send_main(url, method, headers, payload)


    def send_post(self, url, headers, payload):  # Passing parameters
        self.req = requests.post(url=url, headers=headers, json=payload)
        return self.req.json()

    def send_get(self, url, headers, payload):  # Passing parameters
        self.req = requests.get(url=url, headers=headers, params=payload)
        return self.req.json()

    def send_put(self, url, headers, payload):  # Passing parameters
        self.req = requests.put(url=url, headers=headers, payload=payload)
        return self.req.json()

    def send_main(self, url, method, headers, payload):  # According to the protocol, select the method
        if method == 'Get':
            self.req = self.send_get(url, headers, payload)
        elif method == 'Post':
            self.req = self.send_post(url, headers, payload)
        elif method == 'Put':
            self.req = self.send_put(url, headers, payload)
        else:
            print('Method is incorrect')
        return self.req


# if __name__ == '__main__':
#     print(SendMain)


