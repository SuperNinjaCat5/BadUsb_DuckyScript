import os
import requests
import dotenv
import sys
import socket
import platform
import time

debug = True
def debug_print(content):
    if debug == True:
        print(content)

dotenv.load_dotenv()

def discord_post(embed):
    url = os.getenv("URL")
    data = {
        "embeds": [embed]   # embeds must be a list
    }
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

embed = {
    "title": f"System Information - {host_name}",
    "color": 0x00ff00,
    "fields": [
        {"name": "Operating System", "value": operating_system, "inline": True},
        {"name": "OS Version", "value": os_version, "inline": True},
        {"name": "Current User", "value": current_user, "inline": True},
        {"name": "Host Name", "value": host_name, "inline": True},
        {"name": "Public IP", "value": public_ip_address, "inline": False},
        {"name": "Local IP (LAN)", "value": local_ip_address, "inline": False},
        {"name": "CPU Architecture", "value": cpu_architecture, "inline": True},
        {"name": "CPU Core Count", "value": str(cpu_core_count), "inline": True},
    ],
}

discord_post(embed)