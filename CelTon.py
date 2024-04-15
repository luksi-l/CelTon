import requests
import argparse

parser = argparse.ArgumentParser(description='A simple IP and URL info gathering tool')

parser.add_argument('-t', dest='target', required=True, help='Specify IP address or URL')

args = parser.parse_args()

ip_address = args.target


def get_ip_details(ip_address):
    api_url = f"http://ip-api.com/json/{ip_address}"
    reponse = requests.get(api_url)
    if reponse.status_code == 200:
        return reponse.json()
    else:
        return None

ip_details = get_ip_details(ip_address)

if ip_details:
    print("Ip: ", ip_details)