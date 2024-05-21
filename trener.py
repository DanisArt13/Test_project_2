class Test1:
    """ Test """
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return f'{self.text} Test1'
class Test2:
    def __repr__(self):
        return f'{self.text} Test 2'