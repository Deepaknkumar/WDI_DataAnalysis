# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:14:11 2016

@author: Deepak Kumar, 73217151
SDG: Productive Employment and Economic Growth
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
    

##--------------------------------- Target 7% --------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];
t7d = [];
csd = ["GDP per capita","GDP"];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="NY.GDP.PCAP.KD.ZG"):
        if (row[1]=="FCS"):
            fcspd,wr = convToFloat(row[-17:-3],headersData[-17:-3]);
            fcsp = fcspd[-1];
        if (row[1]=="LDC"):
            ldcpd,wr = convToFloat(row[-17:-3],headersData[-17:-3]);
            ldcp = ldcpd[-1];
    if (row[3]=="NY.GDP.MKTP.KD.ZG"):
        if (row[1]=="FCS"):
            fcsd,wr = convToFloat(row[-17:-3],headersData[-17:-3]);
            fcs = fcsd[-1];
        if (row[1]=="LDC"):
            ldcd,wr = convToFloat(row[-17:-3],headersData[-17:-3]);
            ldc = ldcd[-1];
                               
outfile = open("temp.csv","w");
headerContent = "Criteria"+"," + "Value"+"," + "Country Type"+"\n";
outfile.writelines(headerContent);
outfile.writelines(csd[0]+","+str(fcsp) +","+"Countries in fragile and conflict situations"+"\n");
outfile.writelines(csd[1]+","+str(fcs) +","+"Countries in fragile and conflict situations"+"\n");
outfile.writelines(csd[0]+","+str(ldcp) +","+"Least Developed Countries"+"\n");
outfile.writelines(csd[1]+","+str(ldc) +","+"Least Developed Countries"+"\n");
outfile.close();

aeddata = pd.read_csv("temp.csv");

colorcodes = ["#2e9971","#e74c3c"];
sb.set_color_codes("muted");
sb.set_palette(colorcodes);
sb.set_context("poster");

plt.figure(figsize=(20,10),dpi=300)
fig=sb.factorplot(x="Criteria",y="Value",hue="Country Type",data=aeddata,kind="bar",size=12)
plt.ylabel("Percentage(%)")
plt.title("Average Annual growth, 2000-14");
fig.savefig('wbsdgpeeg1.jpg',format='jpg');
infile.close();

##-------------------------- Buisness Registrations ---------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if (row[3]=="IC.BUS.NDNS.ZS"):
        if (row[0]==csd[0]):
            na,nar=convToFloat(row[-15:-1],headersData[-15:-1]);
        if (row[1]=="ECA"):
            eca,ecar=convToFloat(row[-15:-1],headersData[-15:-1]);
        if (row[1]=="LAC"):
            lac,lacr=convToFloat(row[-15:-1],headersData[-15:-1]);
        if (row[1]=="MNA"):
            mena,menar=convToFloat(row[-15:-1],headersData[-15:-1]);
        if (row[1]=="EAP"):
            eap,eapr=convToFloat(row[-15:-1],headersData[-15:-1]);
        if (row[0]==csd[5]):
            sa,sar=convToFloat(row[-15:-1],headersData[-15:-1]);
        if (row[0]==csd[6]):
            ssa,ssar=convToFloat(row[-15:-1],headersData[-15:-1]);
            wr = row;
            
sb.set_palette("bright")
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(20,10),dpi=300);
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
fig.savefig('wbsdgpeeg2.jpg',format='jpg')
infile.close();

