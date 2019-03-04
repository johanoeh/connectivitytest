from model import Test
class TelnetTester:    
    def __init__(self, conns):
        self.conns = conns
        self.testResults = list()
    
    def runTest(self):
         print("\n############## Running telnet tests ################\n")
         for connection in self.conns:
            test = Test()
            test.set_test_method("Telnet socket connect test")
            ip = connection
            port = self.conns[connection]
            print("\n####### connecting to "+ip+" : " + str(port)+" ########\n")
            try:
                tn = telnetlib.Telnet(ip,port)
                print(tn.read_all())
                test.set_message("Successfully connected to: "+connection+":"+conns[connection])
                test.set_result("Success")
                tn.close()
               
            except TimeoutError as e:
                test.set_message("Failed to connect to: "+connection+":"+str(conns[connection])+" with error \n"+"Time Out Error error({0}): {1}".format(e.errno, e.strerror))
                test.set_result("failed")
                print("Time Out Error error({0}): {1}".format(e.errno, e.strerror))
            self.testResults.append(test)
    def get_results(self):
      return self.testResults
