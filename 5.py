weather = {"city" : "Moscow", "temperature" : 25, "wind" : 30}
print(weather["city"])
weather["temperature"] = 40  #взяли значение по ключу температура в словаре погода и присвоили ему значение 40
print(weather["temperature"])
print(len(weather))
print(weather.get("city"))