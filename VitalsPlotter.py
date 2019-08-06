import csv
import matplotlib.pyplot as plt

def extend_limit_list(limit, year):
    new_limit = []
    for i in range(0,len(year)):
        new_limit.append(limit)
    return new_limit

file = '/Users/Brad/Vitals-Sheet1.csv'

limits = {}
limits['Weight'] = [205,246]
limits['Total Cholesterol'] = [200,240]
limits['Triglycerides'] = [150, 200]
limits['LDL'] = [130, 160]
limits['VLDL'] = [30]
limits['HDL'] = [45]

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


plt.plot(year,weight, label='Weight')
plt.plot(year, extend_limit_list(limits['Weight'][0],year), 'y', label='Overweight')
plt.plot(year, extend_limit_list(limits['Weight'][1], year), 'r', label='Obese')
plt.locator_params(axis='x', nbins=5)
plt.legend(bbox_to_anchor=(1.0, 0.75))
plt.ylabel('Weight')
plt.xlabel('Year')
plt.show()

plt.plot(year,total_chl, label='Total')
plt.plot(year, extend_limit_list(limits['Total Cholesterol'][0],year), 'y', label='Borderline')
plt.plot(year, extend_limit_list(limits['Total Cholesterol'][1], year), 'r', label='High')
plt.ylabel('Total Cholesterol')
plt.xlabel('Year')
plt.legend(bbox_to_anchor=(1.0, 0.25))
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,trig, label='Trig')
plt.plot(year, extend_limit_list(limits['Triglycerides'][0],year), 'y', label='Borderline')
plt.plot(year, extend_limit_list(limits['Triglycerides'][1], year), 'r', label='High')
plt.legend(bbox_to_anchor=(1.0, 0.25))
plt.ylabel('Triglycerides')
plt.xlabel('Year')
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,hdl, label='HDL')
plt.ylabel('HDL')
plt.xlabel('Year')
plt.plot(year, extend_limit_list(limits['HDL'][0],year), 'g', label='Minimum')
plt.legend(bbox_to_anchor=(1.0, 0.25))
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,ldl, label='LDL')
plt.ylabel('LDL')
plt.xlabel('Year')
plt.plot(year, extend_limit_list(limits['LDL'][0],year), 'y', label='Borderline')
plt.plot(year, extend_limit_list(limits['LDL'][1], year), 'r', label='High')
plt.legend(bbox_to_anchor=(1.0, 0.25))
plt.locator_params(axis='x', nbins=5)
plt.show()

plt.plot(year,vldl, label='VLDL')
plt.plot(year, extend_limit_list(limits['VLDL'][0],year), 'y', label='Borderline')
plt.legend(bbox_to_anchor=(1.0, 0.25))
plt.ylabel('VLDL')
plt.xlabel('Year')
plt.locator_params(axis='x', nbins=5)
plt.show()
