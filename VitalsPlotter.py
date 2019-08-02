import csv
import matplotlib.pyplot as plt

file = '/Users/Brad/Vitals-Sheet1.csv'

year = []
weight = []
total_chl = []
trig = []
hdl = []
ldl = []
vldl = []
risk = []

reader = csv.DictReader(open(file))
for row in reader:
    year.append(int(row['Year']))
    weight.append(int(row['Weight']))
    total_chl.append(int(row['Total Cholesterol']))
    trig.append(int(row['Triglycerides']))
    hdl.append(int(row['HDL']))
    ldl.append(int(row['LDL']))
    vldl.append(int(row['VLDL']))

plt.figure(figsize=(8,8))

plt.subplot(611)
plt.plot(year,weight)
plt.locator_params(axis='x', nbins=5)
plt.ylabel('Weight')

plt.subplot(612)
plt.plot(year,total_chl)
plt.ylabel('Total Cholesterol')
plt.locator_params(axis='x', nbins=5)

plt.subplot(613)
plt.plot(year,trig)
plt.ylabel('Triglycerides')
plt.locator_params(axis='x', nbins=5)

plt.subplot(614)
plt.plot(year,hdl)
plt.ylabel('HDL')
plt.locator_params(axis='x', nbins=5)

plt.subplot(615)
plt.plot(year,ldl)
plt.ylabel('LDL')
plt.locator_params(axis='x', nbins=5)

plt.subplot(616)
plt.plot(year,vldl)
plt.ylabel('VLDL')
plt.locator_params(axis='x', nbins=5)

plt.show()
