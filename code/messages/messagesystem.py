class MessageSystem:
    class __impl:
        def __init__(self):
            self.channels = {}
            
        def SendMessage(self, message, channels):
            for channel in channels:
                if self.channels.has_key(channel):
                    for listener in self.channels[channel]:
                        listener.HeyListen(message)
                
        def RegesterListener(self, listener, channel):
            if self.channels.has_key(channel):
                self.channels[channel].append(listener)
                return
            self.channels[channel] = [listener]

    __instance = None
    def __init__(self):
        if MessageSystem.__instance is None:
            MessageSystem.__instance = MessageSystem.__impl()
        self.__dict__['_MessageSystem__instance'] = MessageSystem.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
