import time
from datetime import datetime as dt

hosts_path_windows = r"C:/Windows/System32/drivers/etc/hosts"

# hosts_dir = "hosts"
hosts_dir = hosts_path_windows

redirect = "127.0.0.1"

website_list = [
    "www.facebook.com",
    "facebook.com",
    "www.corotos.com.do"
]

from_hour = 7
to_hour = 10

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("Working")
        with open(hosts_dir, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "/n")
    else:
        print("fun")
        with open(hosts_dir, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    
    time.sleep(1)
# > <