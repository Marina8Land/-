from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return f'широта {lat}, долгота: {lon}'
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка: {e}.'


key = '6d816a1105364ba3b749b5cd26ea80d7'
city = "Эквадор"
coordinates = get_coordinates(city, key)
print(f'Координаты гороода {city}: {coordinates}')

"""from opencage.geocoder import OpenCageGeocode

key = '6d816a1105364ba3b749b5cd26ea80d7'
geocoder = OpenCageGeocode(key)

query = u'Bosutska ulica 10, Trnje, Zagreb, Croatia'

# no need to URI encode query, module does that for you
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 45.797095;15.982453;hr;Europe/Belgrade
"""
