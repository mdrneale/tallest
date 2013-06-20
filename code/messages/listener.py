class Listener(object):
    def __init__(self):
        print "default Listener"
        
    def HeyListen(self, message):
        print "This message is not used elsewhere:", message
