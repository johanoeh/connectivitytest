import requests

class URLTester:
	def __init__(self,urls):
		self.urls = urls
	def test(self):
		for x in self.urls:
			print("calling: " +x)
			try:
				r=requests.get(url=x)

				if r.status_code < 300:
					print("Success with status code "+ str(r.status_code ))
				elif r.status_code < 400:
					print("Redirect with status code "+ str(r.status_code ))
				elif r.status_code < 500:
				        print("Bad request with status code "+ str(r.status_code ))
				else:
					print("internal server error with status code "+ str(r.status_code ))
			except requests.exceptions.ConnectionError as e:
				print("connection failed")
			

URLS = ["https://www.st.nu","http://www.kulten.th"]

urlTester = URLTester(URLS)
urlTester.test()
