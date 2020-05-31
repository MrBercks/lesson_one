import copy
weather = {'City':'Москва','temperature':'20','Wind':'восточный'}
print(weather['City'] + '\n') #выводим на экран город

weather['temperature'] = 22 #присваиваем новую пару
print(str(weather['temperature']) + '\n') #выводим на экран новую пару

print(str(len(weather)) + '\n') #выводим на экран количество пар

print(weather.get('Country', 'Not found')) #ищем ключ 'Country'

weather['date'] = '27.05.2017' #добавляем ещё пару

weather1 = copy.copy(weather)
weather1['date'] = '28.05.2017'

weather2 = copy.copy(weather)
weather2['date'] = '29.05.2017'

forecast = [] #объявляем новый список для прогнозов погоды

forecast.append(weather)
forecast.append(weather1)
forecast.append(weather2)

print(forecast)



