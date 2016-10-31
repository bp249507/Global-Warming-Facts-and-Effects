# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:09:56 2016

@author: Binay Prasai
Projects
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


#Part 1 For Temperature Anomaly data of May 2015
df = pd.read_csv('ghcn-m-v1.csv', header=0)
test_df = df[(df['year']==2015) & (df['month']==5)]
test_df = test_df.replace([-9999],[0])
             
lat = np.linspace(87.5,-87.5,36) # np.arange(2.5,180,5)-90
lon = np.linspace(-177.5,177.5,72)
labels = ['150 W','100 W','50 W', '0', '50 E','100 E', '150 E']
labels2 = ['40 N','20 N',0,'20 S','40 S']

temp_anomaly = test_df.values
temp_anomaly = temp_anomaly[:,3:] #temp anomaly matrix

temp_anomaly= temp_anomaly/100
vmin = np.min(temp_anomaly)
vmax = np.max(temp_anomaly)

lon_v, lat_h = np.meshgrid(lon,lat)
cm = plt.get_cmap('jet')
cp = plt.contourf(lon_v,lat_h,temp_anomaly,
                  cmap=cm, 
                  levels=np.linspace(-4,4,50))
                  #levels=np.linspace(math.ceil(vmin),math.ceil(vmax),50))
cb=plt.colorbar(cp, orientation='horizontal', 
                shrink=0.8,
                ticks=[-4,0,4])
plt.ylim(-49,50)
plt.xticks([-150,-100,-50,0,50,100,150],labels)
plt.yticks([40,20,0,-20,-40],labels2)
plt.title('Temperature anomaly (degree Celsius)_ 2015 May')
plt.hlines(0,-177.5,177.5,alpha=0.1)
plt.savefig('Plot1.jpg')
plt.show()

#Part2 Rainfall of 2015 May
df_rainfall=pd.read_csv('TRMM_2015-05-01.csv',header=0)
lat = np.linspace(89.5,-89.5,180) # np.arange(2.5,180,5)-90
lon = np.linspace(-179.5,179.5,360)
labels = ['150 W','100 W','50 W', '0', '50 E','100 E', '150 E']
labels2 = ['40 N','20 N',0,'20 S','40 S']

df_rainfall = df_rainfall.values
df_rainfall = df_rainfall[:,1:] #rainfall matrix

vmin = np.min(df_rainfall)
vmax = np.max(df_rainfall)

lon_v, lat_h = np.meshgrid(lon,lat)
cm = plt.get_cmap('rainbow')
cp = plt.contourf(lon_v,lat_h,df_rainfall,
                  cmap=cm, 
                  levels=np.linspace(0,800,50))
plt.ylim(-49,50)
cb=plt.colorbar(cp, orientation='horizontal', 
                shrink=0.8,
                ticks=[0,400,800])
plt.xticks([-150,-100,-50,0,50,100,150],labels)
plt.yticks([40,20,0,-20,-40],labels2)
plt.title('Rainfall (mm)_ 2015 May')
plt.hlines(0,-179.5,179.5,alpha=0.1)
plt.savefig('Plot2.jpg')
plt.show()