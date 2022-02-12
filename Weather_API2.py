import requests
import json
def weather():
    try:
        url2 = "https://us-weather-by-zip-code.p.rapidapi.com/getweatherzipcode"
        headers2 = {
            'x-rapidapi-host': "us-weather-by-zip-code.p.rapidapi.com",
            'x-rapidapi-key': "cf4818eb5amshc6c673cb0b5a4e5p1a5d78jsn73a0d20bd5cf"
            }
        response2 = requests.request("GET", url2, headers=headers2, params=querystring)
        body2 = response2.json()
###print(body:{"City":{...}, "State":{...}, "TempF":{...}, "TempC":{...}, "Weather":{...}, "WindMPH":{...},
# "WindDir":{...}, "RelativeHumidity":{...}, "VisibilityMiles":{...}, "Code":{...}, "Credits":{...}})]
        return body2
    except:
         pass
while True:
    zip_str = input("input zip: ")
    if zip_str:
        zip_number = int(zip_str)
        querystring = {"zip": zip_number}
        wea = weather()
        for w in wea:
            print(w, '---', wea[w])
    else:
        break