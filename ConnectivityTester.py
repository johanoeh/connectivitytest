import telnetlib
import subprocess
import os
from httpreq import URLTester
from model import Test
from pingtest import PingTester
from testproperties import TestProperty
from propertyreader import PropertyReader
     

def displayTest(tests):
        for test01 in tests:
            print("Test run ###################################################")
            print("Test method: "+test01.get_test_method()+"\nResult message: \n"+test01.get_message()+"\nResult: " + test01.get_result()+"\n")
            
conns = dict()
conns["10.20.223.175"] = 10003
conns["10.20.223.179"] = 10003
conns["192.168.1.0"] = 10003


#pingTester = PingTest(conns)
#pingTester.runTest()

#tester = TelnetTester(conns)
#tester.runTest()

URLS = dict()

urlTester = URLTester(URLS)
urlTester.test()
displayTest(urlTester.get_results())
reader = PropertyReader("tests.txt")
reader.read()

props = reader.get_properties()
for x in props:
    print(x.to_string())




    

