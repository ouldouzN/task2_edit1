import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import csv
import statistics


#step:1
#making dataframe and analyizing
data=pd.read_csv('AdmissionPredict.csv')
print(data.describe())
print(data.info())

#print(data['LOR'])

#step:2
serial_nan=data['Serial No.'].isna().sum()
gre_nan=data['GRE Score'].isna().sum()
tofel_nan=data['TOEFL Score'].isna().sum()
university_nan=data['University Rating'].isna().sum()
sop_nan=data['SOP'].isna().sum()
#lor_nan=data['LOR'].isna().sum()
cgpa_nan=data['CGPA'].isna().sum()
reasearch_nan=data['Research'].isna().sum()
admit_nan=data['Chance of Admit'].isna().sum()

#step:3
#filling missing data with the mean 
serial_mean=data['Serial No.'].mean()
gre_mean=data['GRE Score'].mean()
tofel_mean=data['TOEFL Score'].mean()
university_mean=data['University Rating'].mean()
sop_mean=data['SOP'].mean()
#lor_mean=data['LOR'].mean
cgpa_mean=data['CGPA'].mean()
research_mean=data['Research'].mean()
admit_mean=data['Chance of Admit'].mean()

data['Serial No.'].fillna(serial_mean,inplace=True)
data['GRE score'].fillna(gre_mean,inplace=True)
data['TOEFl Score'].fillna(tofel_mean,inplace=True)
data['University Rating'].fillna(university_mean,inplace=True)
data['SOP'].fillna(sop_mean,inplace=True)
#data['LOR'].fillna(lor_mean,inplace=True)
data['CGPA'].fillna(cgpa_mean,inplace=True)
data['Research'].fillna(research_mean,inplace=True)
data['Chance of Admit'].fillna(admit_mean,inplace=True)

#filling missing data with the median
serial_med=statistics.median(data['Serial No.'])
gre_med=statistics.median(data['GRE Score'])
toefl_med=statistics.median(data['TOEFL Score'])
uni_med=statistics.median(data['University Rating'])
sop_med=statistics.median(data['SOP'])
#lor_med=statistics.median(data['LOR'])
cgpa_med=statistics.median(data['CGPA'])
research_med=statistics.median(data['Research'])
admit_med=statistics.median(data['Chance of Admit'])


data['Serial No.'].fillna(serial_med,inplace=True)
data['GRE score'].fillna(gre_med,inplace=True)
data['TOEFl Score'].fillna(toefl_med,inplace=True)
data['University Rating'].fillna(uni_med,inplace=True)
data['SOP'].fillna(sop_med,inplace=True)
#data['LOR'].fillna(lor_med,inplace=True)
data['CGPA'].fillna(cgpa_med,inplace=True)
data['Research'].fillna(research_med,inplace=True)
data['Chance of Admit'].fillna(admit_med,inplace=True)

#step:4
fig,axs=plt.subplots(4,2)
plt.figure()
axs[0,0]=plt.scatter(data['Serial No.'],data['Chance of Admit'])
axs[0,1]=plt.scatter(data['GRE score'],data['Chance of Admit'])
axs[0,2]=plt.scatter(data['TOEFL Score'],data['Chance of Admit'])
axs[0,3]=plt.scatter(data['University Rating'],data['Chance of Admit'])
axs[1,0]=plt.scatter(data['SOP'],data['Chance of Admit'])
#axs[1,1]=plt.scatter(data['LOR'],data['Chance of Admit'])
axs[1,2]=plt.scatter(data['CGPA'],data['Chance of Admit'])
axs[1,3]=plt.scatter(data['Research'],data['Chance of Admit'])
plt.show()

