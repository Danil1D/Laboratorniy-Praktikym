import matplotlib.pyplot as plt

potato_price = [45.00,45.00,40.00]
cabbage_price = [50.00,45.00,40.00]
onion_price = [70.00,60.00,60.00]
average_price = [55.00,50.00,46.67]
date = ["02.11.2016","14.11.2016","22.11.2016"]
plt.plot(date,potato_price,label = "Картопля 'Бесарабський' ")
plt.plot(date,cabbage_price,label = "Капуста 'Бесарабський' ")
plt.plot(date,onion_price,label = "Цибуля 'Бесарабський' ")
plt.plot(date,average_price,label = "Середня ціна 'Бесарабський' ")
plt.xlabel("Дата")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)


potato_price = [35.00, 35.00, 40.00]
cabbage_price = [30.00,35.00,35.00]
onion_price = [45.00,45.00,60.00]
average_price = [36.67,38.33,45.00]
date = ["02.11.2016","14.11.2016","22.11.2016"]
plt.plot(date,potato_price,label = "Картопля 'Володимирський' ")
plt.plot(date,cabbage_price,label = "Капуста 'Володимирський' ")
plt.plot(date,onion_price,label = "Цибуля 'Володимирський' ")
plt.plot(date,average_price,label = "Середня ціна 'Володимирський' ")
plt.xlabel("Дата")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def showplot():
    plt.show()