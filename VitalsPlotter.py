import csv
import matplotlib.pyplot as plt

def extend_limit_list(limit, year):
    new_limit = []
    for i in range(0,len(year)):
        new_limit.append(limit)
    return new_limit

file = '/Users/Brad/Vitals-Sheet1.csv'

limits = {}
limits['Weight'] = [200,240]
limits['Total Cholesterol'] = [200,240]

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


plt.plot(year,weight)
plt.plot(year, extend_limit_list(limits['Weight'][0],year), 'y')
plt.plot(year, extend_limit_list(limits['Weight'][1], year), 'r')
plt.locator_params(axis='x', nbins=5)
plt.ylabel('Weight')
plt.show()

plt.plot(year,total_chl)
plt.plot(year, extend_limit_list(limits['Total Cholesterol'][0],year), 'y')
plt.plot(year, extend_limit_list(limits['Total Cholesterol'][1], year), 'r')
plt.ylabel('Total Cholesterol')
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,trig)
plt.ylabel('Triglycerides')
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,hdl)
plt.ylabel('HDL')
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,ldl)
plt.ylabel('LDL')
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,vldl)
plt.ylabel('VLDL')
plt.locator_params(axis='x', nbins=5)
plt.show()
