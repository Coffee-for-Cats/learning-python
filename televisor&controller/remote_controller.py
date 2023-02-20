class RemoteController:
    def __init__(self, tv):
        self.tv = tv

    def increase_volume(self, value):
        self.tv.increase_volume(value)

    def decrease_volume(self, value):
        self.tv.decrease_volume(value)

    def change_chanel(self, chanel):
        self.tv.change_chanel(chanel)

    def tune_chanel(self, chanel):
        self.tv.tune_chanel(chanel)
