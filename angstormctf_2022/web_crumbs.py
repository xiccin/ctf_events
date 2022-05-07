from requests import get,exceptions
from os import system

clear = lambda: system('clear')


url = link = "https://crumbs.web.actf.co/"
timeouts = 0
redirects = -1
flag = ""

while True:

    try:
        r = get(link, timeout=0.5)
        link = url + (r.text[6::])

        if (r.text == "Broke the trail of crumbs..."):
            break

        if (r.text!=flag):
            redirects+=1

        flag = r.text

        clear()
        print(f"redirects\t: {redirects}\ngoing to\t: {link}\ntimeouts\t: {timeouts}")

    except exceptions.Timeout:
        timeouts+=1

clear()
print(f"redirects\t: {redirects}\ntimeouts\t: {timeouts}\nflag\t\t: {flag}")
