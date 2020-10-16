import matplotlib.pyplot as plt
import requests

fetch = requests.get("https://atlas.jifo.co/api/connectors/85b110ec-591a-409e-90da-de79e75543aa")

res = fetch.json()

casesTime = res['data'][0]
days = [0]
cases = [0]
for day in casesTime:
    if day[1]!="Nových případů za den":
            days.append(days[len(days)-1]+1)
            cases.append(int(day[1]))
            print(days)
            #plt.scatter(day, int(day[1]))
#plt.scatter(days, cases)
changes = []
for daily in range(len(cases)):
    if cases[daily]!=cases[-1] and cases[daily+1] != 0 and cases[daily] != 0:
        changes.append(cases[daily+1]/cases[daily])
plt.show()
print(changes)