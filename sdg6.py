# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:48:29 2016

@author: Deepak Kumar, 73217151
SDG: Industry, Innovation and Infrastructure
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

def convToFloat(inputList,xval):
    outputList = [];
    outputxval = [];
    for i in range(0,len(inputList)):
        if(inputList[i]!=""):
            outputList.append(float(inputList[i]));
            outputxval.append(float(xval[i]));
    return outputList,outputxval;

##---------------------- Manufacturing value added ---------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];
csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="NV.IND.MANF.ZS"):
        if (row[0]==csd[0]):
            na,nar=convToFloat(row[-27:-3],headersData[-27:-3]);
        if (row[0]==csd[1]):
            eca,ecar=convToFloat(row[-27:-3],headersData[-27:-3]);
        if (row[0]==csd[2]):
            lac,lacr=convToFloat(row[-27:-3],headersData[-27:-3]);
        if (row[0]==csd[3]):
            mena,menar=convToFloat(row[-27:-3],headersData[-27:-3]);
        if (row[0]==csd[4]):
            eap,eapr=convToFloat(row[-27:-3],headersData[-27:-3]);
        if (row[0]==csd[5]):
            sa,sar=convToFloat(row[-27:-3],headersData[-27:-3]);
        if (row[0]==csd[6]):
            ssa,ssar=convToFloat(row[-27:-3],headersData[-27:-3]);
        if (row[0]==csd[7]):
            wd,wy=convToFloat(row[-27:-3],headersData[-27:-3]);
            wr = row;
            
sb.set_palette("bright")
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(20,10),dpi=300);
plt.plot(wy,wd,label="World Data")
plt.plot(ssar,ssa,label="Sub-Saharan Africa")
plt.plot(sar,sa,label="South Asia")
plt.plot(menar,mena,label="Middle East and North Africa")
plt.plot(ecar,eca,label="Europe and Central Asia")
plt.plot(eapr,eap,label="East Asia and Pacific")
sb.set_context("notebook",rc={"lines.linewidth":2.7})
plt.plot(lacr,lac,label="Latin America & Caribbean")
plt.plot(nar,na,label="North America");
plt.xlabel("Years")
plt.ylabel(wr[2])
plt.legend();
plt.title(wr[2] + "Vs Years")
fig.savefig('wbsdgiii1.jpg',format='jpg')
infile.close();

##------------------------ R&D expenditure-------------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
csd = ["China","Brazil","India","South Africa","Russian Federation"];

for row in csvdata:
    if (row[3]=="GB.XPD.RSDV.GD.ZS"):
        if (row[0]==csd[0]):
            china,chinar=convToFloat(row[-10:-3],headersData[-10:-3]);
        if (row[0]==csd[1]):
            brazil,brazilr=convToFloat(row[-10:-3],headersData[-10:-3]);
        if (row[0]==csd[2]):
            India,Indiar=convToFloat(row[-10:-3],headersData[-10:-3]);
        if (row[0]==csd[3]):
            sa,sar=convToFloat(row[-10:-3],headersData[-10:-3]);
        if (row[0]==csd[4]):
            rf,rfr=convToFloat(row[-10:-3],headersData[-10:-3]);
            wr = row;
            
sb.set_palette("bright")
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(20,10),dpi=300);
plt.plot(chinar,china,label="China")
plt.plot(brazilr,brazil,label="Brazil")
plt.plot(Indiar,India,label="India")
plt.plot(sar,sa,label="South Africa")
plt.plot(rfr,rf,label="Russian Federation")
plt.xlabel("Years")
plt.ylabel(wr[2])
plt.legend();
plt.title(wr[2] + "Vs Years")
fig.savefig('wbsdgiii2.jpg',format='jpg')
infile.close();