from testproperties import TestProperty
class PropertyReader:
    def __init__(self,file):
        self.file = file
        self.props = list()
    def read(self):
        f = open(self.file, "r")
        for x in f:
            print(x)
            if "#" in x:
                continue  
            split = x.split(",")
            properties = TestProperty()
            properties.set_test_method(split[0])
            properties.set_url(split[1])
            properties.set_ip(split[2])
            properties.set_port(str(split[3]))
            print(properties.to_string())
            self.props.append(properties)
    def get_properties(self):
        return self.props

       
