# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:26:20 2016

@author: Deepak Kumar, 73217151
SDG: Sustainable cities and Communities

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

##------------------ Share of urban population living in slums-----------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];
csd = ["Central African Republic","Mozambique","Rwanda","Mali","Sub-Saharan Africa"];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="EN.POP.SLUM.UR.ZS"):
        if (row[0]==csd[0]):
            car,carr=convToFloat(row[-27:-1],headersData[-27:-1]);
        if (row[0]==csd[1]):
            moz,mozr=convToFloat(row[-27:-1],headersData[-27:-1]);
        if (row[0]==csd[2]):
            rw,rwr=convToFloat(row[-27:-1],headersData[-27:-1]);
        if (row[0]==csd[3]):
            ml,mlr=convToFloat(row[-27:-1],headersData[-27:-1]);
        if (row[0]==csd[4]):
            ssa,ssar=convToFloat(row[-27:-1],headersData[-27:-1]);
            wr = row;
            
sb.set_palette("bright")
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(20,10),dpi=300);
plt.plot(ssar,ssa,label="Sub-Saharan Africa")
plt.plot(carr,car,label="Central African Republic")
plt.plot(mozr,moz,label="Mozambique")
plt.plot(rwr,rw,label="Rwanda")
plt.plot(mlr,ml,label="Mali")
plt.xlabel("Years")
plt.ylabel(wr[2])
plt.legend();
plt.title(wr[2] + "Vs Years")
fig.savefig('wbsdgscc1.jpg',format='jpg')
infile.close();

##------------------- Mean annual concentration of particles -------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if (row[3]=="EN.ATM.PM25.MC.M3"):
        if (row[0]==csd[0]):
            na=[float(row[-27]),float(row[-4])];
        if (row[0]==csd[1]):
            eca=[float(row[-27]),float(row[-4])];
        if (row[0]==csd[2]):
            lac=[float(row[-27]),float(row[-4])];
        if (row[0]==csd[3]):
            mena=[float(row[-27]),float(row[-4])];
        if (row[0]==csd[4]):
            eap=[float(row[-27]),float(row[-4])];
        if (row[0]==csd[5]):
            sa=[float(row[-27]),float(row[-4])];
        if (row[0]==csd[6]):
            ssa=[float(row[-27]),float(row[-4])];
        if (row[0]==csd[7]):
            wd=[float(row[-27]),float(row[-4])];
            wr = row;
            
aed = [na,eca,lac,mena,eap,sa,ssa,wd];
outfile = open("temp.csv","w");
headerContent = "Divisions"+"," + "value"+"," + "year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(csd)):
    outfile.writelines(csd[i]+","+str(aed[i][0]) +","+"1990"+"\n");
    outfile.writelines(csd[i]+","+str(aed[i][1]) +","+"2013"+"\n");
outfile.close();

aeddata = pd.read_csv("temp.csv");

colorcodes = ["#e74c3c","#2e9971"];
sb.set_color_codes("bright");
sb.set_palette(colorcodes);
sb.set_context("poster")

plt.figure(figsize=(20,10),dpi=300)
fig=sb.factorplot(x="Divisions",y="value",hue="year",data=aeddata,kind="bar",size=20)
plt.xlabel("Sub continent Divisions");
plt.ylabel(wr[2])
plt.title(wr[2]+ "in different areas of world");
fig.savefig('wbsdgscc2.jpg',format='jpg');
infile.close();
