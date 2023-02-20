from televisor import *
from remote_controller import *

my_televisor = Televisor("Toyota", "Tube")
my_controller = RemoteController(my_televisor)

# 20
print(my_televisor.volume)

# 100, max
my_controller.increase_volume(999)
print(my_televisor.volume)

# 0, min
my_controller.decrease_volume(9999)
print(my_televisor.volume)

my_controller.tune_chanel("Globo")
my_controller.tune_chanel("Bandeirantes")
my_controller.tune_chanel("CNT")

print(my_televisor.chanel_list)

# Globo
my_controller.change_chanel("Globo")
print(my_televisor.current_chanel)

# "erro" que ainda não é erro
my_controller.change_chanel("TNT")
