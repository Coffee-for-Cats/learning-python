class Televisor:
    def __init__(self, fab, model):
        self.fabricant = fab
        self.model = model
        self.current_chanel = None
        self.chanel_list = []
        self.volume = 20

    def increase_volume(self, value):
        if self.volume + value <= 100:
            self.volume += value
        else:
            self.volume = 100

    def decrease_volume(self, value):
        if self.volume - value >= 0:
            self.volume -= value
        else:
            self.volume = 0

    def change_chanel(self, chanel):
        if chanel in self.chanel_list:
            self.current_chanel = chanel
        else:
            print(f'ERRO: o canal "{chanel}" ainda não foi sintonizado!')

    def tune_chanel(self, chanel):
        if chanel not in self.chanel_list:
            # isso ta errado por que strings são arrays também! Assim ele adiciona cada letra individualmente
            # self.chanel_list += chanel
            # por isso, eu preciso dizer para ele colocar especificamente cada item:
            self.chanel_list.append(chanel)
