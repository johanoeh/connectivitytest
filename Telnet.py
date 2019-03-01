import telnetlib
import subprocess
import os


class PingTest:
    
  def __init__(self, conns):
        self.conns = conns
  def runTest(self):
       print("\n############## Running ping tests ################\n")
       for connection in self.conns:
            print("##################################################\n")
            ip = connection
            op = subprocess.check_output(["ping",ip, "-n","1"])
            x = str(op)
            y = x.split("\\r\\n")
            for i in y:
                if not ('b\'' in i) and not("'" in i):
                    print(i)
            print("\n##################################################\n")
                    
class TelnetTester:
    
    def __init__(self, conns):
        self.conns = conns
    
    def runTest(self):
         print("\n############## Running telnet tests ################\n")
         for connection in self.conns:
            ip = connection
            port = self.conns[connection]
            print("\n####### connecting to "+ip+" : " + str(port)+" ########\n")
            try:
                tn = telnetlib.Telnet(ip,port)
                tn.interact()
            except TimeoutError as e:
                print("Connection failed with error")
                print ("Time Out Error error({0}): {1}".format(e.errno, e.strerror))
            
    
conns = dict()
conns["10.20.223.175"] = 10003
conns["10.20.223.179"] = 10003

pingTester = PingTest(conns)
pingTester.runTest()

tester = TelnetTester(conns)
tester.runTest()



