class Listener(object):
    def __init__(self):
        print "default Listener"
        
    def HeyListen(self, message):
        print "This message is not used elsewhere:", message

# example listener
if __name__ == "__main__":
	l = Listener()
	import messagesystem
	messagesystem.MessageSystem().RegesterListener(l,"example")
	messagesystem.MessageSystem().SendMessage("message example",["example"])
