class TestProperty:
    def __init__(self):
        self.test_method= ""
        self.ip = ""
        self.port = ""
        self.url =""
    def set_test_method(self, test_method):
        self.test_method = test_method
    def get_test_method(self):
        return self.test_method
    def get_ip(self):
        return self.ip
    def set_ip(self, ip):
        self.ip = ip
    def get_port(self):
        return self.port
    def set_port(self, port):
        self.port = port
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url=url
    def to_string(self):
        return "TestProperties[test_method={}, ip={}, port={}, url={}]".format(self.test_method, self.ip, self.port, self.url)
    
    
