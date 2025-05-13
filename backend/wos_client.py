import requests
import os

WOS_API_KEY=os.getenv("WOS_API_KEY")
BASE_URL="https://api.clarivate.com/apis/wos-starter/v1/documents"

def fetch_wos_data(query,limit=10):
    headers = {
        "X-Apikey":WOS_API_KEY
    }

    params = {
        "q":query,
        "db":'WOS',
        "limit":limit
    }

    response = requests.get(BASE_URL,headers=headers,params=params)
    response.raise_for_status()

    return response.json()