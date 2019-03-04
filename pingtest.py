from model import Test
class PingTester:
    
  def __init__(self, conns):
        self.conns = conns
        self.testResults = list()
  def runTest(self):
       for connection in self.conns:
            test = Test()
            test.set_test_method("ping")
            resp=""
            ip = connection
            try:
              op = subprocess.check_output(["ping",ip, "-n","3"])
              x = str(op)
              y = x.split("\\r\\n")
              for i in y:
                  if not ('b\'' in i) and not("'" in i):
                      resp+=i+"\n"
              test.set_message(resp)
              test.set_result("Success")
              self.testResults.append(test)
            except subprocess.CalledProcessError as e:
              print(e)
              test.set_message("Request failed")
              test.set_result("failed")
              self.testResults.append(test)
              
  def get_results(self):
    return self.testResults
