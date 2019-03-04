import requests
from model import Test

class URLTester:
        def __init__(self,urls):
                self.urls = urls
                self.testResults = list()
        def test(self):
                for x in self.urls:
                        test=Test()
                        print("calling: " +x)
                        try:
                                r=requests.get(url=x)

                                if r.status_code < 300:
                                        test.set_message("Success with status code "+ str(r.status_code ))
                                        test.set_result("Success")
                                elif r.status_code < 400:
                                        test.set_message("Redirect with status code "+ str(r.status_code ))
                                        test.set_result("failed")
                                elif r.status_code < 500:
                                        test.set_message("Bad request with status code "+ str(r.status_code ))
                                        test.set_result("failed")
                                else:
                                        test.set_message("internal server error with status code "+ str(r.status_code ))
                                        test.set_result("failed")
                        except requests.exceptions.ConnectionError as e:
                                test.set_message("connection failed")
                        self.testResults.append(test)
        def get_results(self):
                return self.testResults
	
			



