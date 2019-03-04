class Test:
  def __init__(self):
    self.testMethod=""
    self.message=""
    self.result=""
    self.ip=""
  def set_message(self, msg):
    self.message=msg
  def get_message(self):
    return self.message
  def set_test_method(self,testMethod):
    self.testMethod = testMethod
  def get_test_method(self):
    return self.testMethod
  def get_result(self):
    return self.result
  def set_result(self, result):
    self.result=result
  def get_ip(self):
    return self.ip
  def set_ip(self, ip):
    self.ip=ip
