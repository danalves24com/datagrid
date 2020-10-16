import matplotlib.pyplot as plt
data = [8232, 9214, 7412, 5312, 7812]
r = [0]
p = []
preds = [0]
for dat in range(len(data)):
    if dat+1!=len(data):
        r.append(data[dat+1]/data[dat])

for rate in range(len(r)-1):
    p.append(data[rate+1]/data[rate+1]*r[rate])
    preds.append(data[rate+1]*r[rate])

mn = sum(p) / len(p) 
correction = [0]
for dat in range(len(data)-1):
    correction.append(data[dat]*(mn*r[dat]))
print(p)
print(preds)
plt.plot(data)
plt.plot(preds)
plt.plot(correction)
plt.show()