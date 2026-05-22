import requests
class APIClient:

    BASE_URL = (
        "https://jsonplaceholder.typicode.com"
    )

    def get(self , endpoint, headers = None):
        return requests.get(
            f"{self.BASE_URL}{endpoint}",
            headers=headers
        )
    
    def post(self, endpoint, payload, headers = None):
        return requests.post(
            f"{self.BASE_URL}{endpoint}",
            json = payload,
            headers = headers
        )
    def put(self, endpoint,payload, headers = None):
        return requests.put(
            f"{self.BASE_URL}{endpoint}",
            json=payload,
            headers=headers
        )
    def delete(self, endpoint, headers= None):

        return requests.delete(
            f"{self.BASE_URL}{endpoint}",
            headers= headers
        )