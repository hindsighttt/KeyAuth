import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_json = response.json()
    return ip_json['ip']

ip_address = get_public_ip()