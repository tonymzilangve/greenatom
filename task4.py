import requests

public_ip = requests.get("https://ifconfig.me").text

print(public_ip)
