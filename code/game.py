from window.window import Window

class Game(Window):
    def __init__(self, state):
        self.state = state
        super(Game, self).__init__(720, 512, "Tallest")

    def update(self, timestep):
        self.state = self.state.update(timestep)
        return self.state != None

    def present(self):
        if self.state != None:
            self.state.present(self.surface)
        super(Game, self).present()

if __name__ == "__main__":
    import states
    g=Game(states.MainState())
