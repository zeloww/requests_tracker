import json, os
from random import choice

try:
	import requests

except:
	os.system("pip install requests")
	import requests

try:
	from bs4 import BeautifulSoup

except:
	os.system("pip install bs4")
	from bs4 import BeautifulSoup

zelow = """
██████╗ ███████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗███████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝█████╗  ██║   ██║██║   ██║█████╗  ███████╗   ██║   ███████╗       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ╚════██║       ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║   ███████║       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                            1 > Requests History  |  2 > IPlogger Jammer                                 by Zelow#999
                                                  3 > Whois info  |  4 > Short URL
"""

proxies_http = []
proxies_https = []

def getproxies():
	 
	print("One second please...\n")

	http_scrapeds = 0
	url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=50"
	request = requests.get(url).text

	for proxy in request.split('\n'):
		proxies = {
			"http": "http://"  + proxy.replace("\r", "")
		}

		try:
			requests.get("http://info.cern.ch/", proxies=proxies)
			proxies_http.append(proxy.replace("\r", ""))
			http_scrapeds += 1
			print(proxy)

			if http_scrapeds == 4:
				break

		except:
			pass

	https_scrapeds = 0
	url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=50"
	request = requests.get(url).text

	for proxy in request.split('\n'):
		proxies = {
			"https": "http://"  + proxy.replace("\r", "")
		}

		try:
			requests.get("https://google.com/", proxies=proxies)
			proxies_https.append(proxy.replace("\r", ""))
			https_scrapeds += 1
			print(proxy)

			if https_scrapeds == 4:
				break

		except:
			pass

def request_history():
	url = input("Enter the url >>> ")
	auto_proxies = input("Do you want auto proxies? [y/n] >>> ")

	headers = {
		"Content-Type": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
	}

	if auto_proxies.lower() in ["y", "yes"]:

		proxies = {
			"http": "http://" + choice(proxies_http),
			"https": "http://" + choice(proxies_https),
		}

		response = requests.get(url=url, proxies=proxies, headers=headers, allow_redirecst=True)

	else:
		response = requests.get(url=url, headers=headers, allow_redirects=True)

	if response.history:
		for link in response.history:
			print(f"[{link.status_code}] {link.url}")

		print("\nDown.")

	else:
		print("No redirections!")

	input()
	main()

def jammer():
	i = 0
	url = input("\nEnter the url >>> ")
	auto_proxies = input("Do you want auto proxies? [y/n] >>> ")

	while True:
		counter = input("Numbers of requests? (<= 50) >>> ")

		try:
			counter = int(counter)

		except:
			print("Invalid number!")

		if counter <= 50:
			break

		else:
			print("Invalid number!")

	while i != counter:

		headers = {
			"Content-Type": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
		}

		if auto_proxies.lower() in ["y", "yes"]:

			proxies = {
				"http": "http://" + choice(proxies_http),
				"https": "http://" + choice(proxies_https),
			}

			try:
				response = requests.get(url=url, proxies=proxies, headers=headers)
				print("[Successfully] " + str(proxies["http"]) +  " and " + str(proxies["https"]))
				i += 1

			except:
				print("[Error] " + str(proxies["http"]) +  " and " + str(proxies["https"]))


		else:
			try:
				response = requests.get(url=url, headers=headers)
				print("[Successfully]")
				i += 1

			except:
				print("[Error]")

	print("\nDown\n" + str(i) + " submitted requests")
	input()
	main()

def whoisinfo():
	link = input("Enter the url >>> ")
	url = "http://www.whois-raynette.fr/whois/" + link

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	request = str(soup.find_all("div", {"class": "whois_section_content"}))
	replace_list = ['[<div class="whois_section_content" style="width:478px; margin:0 auto;">', '            ', '    </div>]', '<br/>']

	for to_replace in replace_list:
		request = request.replace(to_replace, '')

	print(request)
	input()
	main()

def shorturl():
	link = input("Enter the url >>> ")
	url = f"https://api.shrtco.de/v2/shorten?url={link}/very/long/link.html"

	response = requests.get(url)
	print(response.text)
	print("\n Your short link for: " + link + " is shrtco.de/" + json.loads(response.text)["result"]["code"])

	input()
	main()

def main():
	os.system("color d")
	while True:
		os.system("cls")
		print(zelow)

		try:
			choice = int(input(">>> "))
		except:
			continue

		if choice == 1:
			request_history()
			break

		elif choice == 2:
			jammer()
			break

		elif choice == 3:
			whoisinfo()
			break

		elif choice == 4:
			shorturl()
			break
		elif choice == 5:
			subdomain()
			break

		else:
			pass

getproxies()
main()
