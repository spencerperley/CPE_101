

aqiRanges = (0,50, 100, 150, 200, 300, 500)
aqiDescriptions = ("Good", "Moderate", "Unhealthy for Sensitive Groups",
                  "Unhealthy", "Very Unhealthy", "Hazardous")

aqiDescription = ""



pm25ranges = (0, 12, 35.4, 55.4, 150.4, 250.4, 500.4)
pm10ranges = (0, 54, 154, 254, 354, 424, 604)
no2ranges = (0, 53, 100, 360, 649, 1249, 2049)
so2ranges = (0, 35, 75, 185, 304, 604, 1004)
coranges = (0, 4.4, 9.4, 12.4, 15.4, 30.4, 50.4)


iHigh, iLow, cHigh, cLow, cP = 0, 0, 0, 0, 0


pollutantRanges = {"PM2.5":pm25ranges,"PM10":pm10ranges,"NO2":no2ranges,"SO2":so2ranges,"CO":coranges}
keys = dict.keys(pollutantRanges)

location = input("Where is this measurement taken from? ")


def takeInput(upperBound, message):
    while True:
        tempinput = int(input(message))
        if (tempinput < 0) or (tempinput > upperBound):
            print(
                f"Entered value is out of range, please use a value between 0 and {upperBound}")
        else:
            break

    return (tempinput)


def calculateAQI(name, ranges):
    cP = takeInput(ranges[5], str(
        f"Enter the value for the {name} concentration : "))

    index = 0
    for upper in ranges:

        if cP < upper:
            cHigh = upper
            cLow = ranges[index - 1]
            iHigh = aqiRanges[index]
            iLow = aqiRanges[index - 1]

            break
        index += 1

    
    return(((iHigh-iLow)/(cHigh-cLow)*(cP-cLow))+iLow)

results = []
endMessages = []

for key in keys:
    result = calculateAQI(key,pollutantRanges[key])
    endMessages.append(f"The Air Quality Index of {key} is {result}")
    results.append(result)

maxAqi = max(results)

index = 0
for upper in aqiRanges:
    if maxAqi < upper:
        print(f"The Air Quality Index in {location} is {maxAqi}, this is {aqiDescriptions[index - 1]}" )
        break
    index += 1

for endMessage in endMessages:
    print(endMessage)