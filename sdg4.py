# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:05:37 2016

@author: Deepak Kumar, 73217151
SDG: Affordable and Clean Energy
"""
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

##------------------------ Access to electricity ------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];
aed = [];
csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];
na=[];
eca = [];
lac = [];
mena = [];
eap = [];
sa = [];
ssa = [];
wd = [];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="EG.ELC.ACCS.ZS"):
        if (row[0]==csd[0]):
            na=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[1]):
            eca=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[2]):
            lac=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[3]):
            mena=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[4]):
            eap=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[5]):
            sa=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[6]):
            ssa=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[7]):
            wd=[float(row[-27]),float(row[-5])];

aed = [na,eca,lac,mena,eap,sa,ssa,wd];
outfile = open("temp.csv","w");
headerContent = "Divisions"+"," + "value"+"," + "year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(csd)):
    outfile.writelines(csd[i]+","+str(aed[i][0]) +","+"1990"+"\n");
    outfile.writelines(csd[i]+","+str(aed[i][1]) +","+"2012"+"\n");
outfile.close();

aeddata = pd.read_csv("temp.csv");

colorcodes = ["#e74c3c","#2e9971"];
sb.set_color_codes("muted");
sb.set_palette(colorcodes);
sb.set_context("poster");

plt.figure(figsize=(20,10),dpi=300)
fig=sb.factorplot(x="Divisions",y="value",hue="year",data=aeddata,kind="bar",size=20)
plt.xlabel("Sub continent Divisions");
plt.ylabel("Percentage(%)")
plt.title("Access to Eclectricity(% of population)");
fig.savefig('wbsdgace1.jpg',format='jpg');
infile.close();

##-------------- Renewable energy plot ---------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
red = [];
csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if (row[3]=="EG.FEC.RNEW.ZS"):
        if (row[0]==csd[0]):
            na=[float(row[-27]),float(row[-17]),float(row[-5])];
        if (row[0]==csd[1]):
            eca=[float(row[-27]),float(row[-17]),float(row[-5])];
        if (row[0]==csd[2]):
            lac=[float(row[-27]),float(row[-17]),float(row[-5])];
        if (row[0]==csd[3]):
            mena=[float(row[-27]),float(row[-17]),float(row[-5])];
        if (row[0]==csd[4]):
            eap=[float(row[-27]),float(row[-17]),float(row[-5])];
        if (row[0]==csd[5]):
            sa=[float(row[-27]),float(row[-17]),float(row[-5])];
        if (row[0]==csd[6]):
            ssa=[float(row[-27]),float(row[-17]),float(row[-5])];
        if (row[0]==csd[7]):
            wd=[float(row[-27]),float(row[-17]),float(row[-5])];
aed = [na,eca,lac,mena,eap,sa,ssa,wd];
outfile = open("temp.csv","w");
headerContent = "Divisions"+"," + "value"+"," + "year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(csd)):
    outfile.writelines(csd[i]+","+str(aed[i][0]) +","+"1990"+"\n");
    outfile.writelines(csd[i]+","+str(aed[i][1]) +","+"2000"+"\n");
    outfile.writelines(csd[i]+","+str(aed[i][2]) +","+"2012"+"\n");
outfile.close();

aeddata = pd.read_csv("temp.csv");

colorcodes = ["#e74c3c","#2eBBAA","#2e9971"];
sb.set_color_codes("muted");
sb.set_palette(colorcodes);
sb.set_context("poster")

plt.figure(figsize=(20,10),dpi=300)
fig=sb.factorplot(x="Divisions",y="value",hue="year",data=aeddata,kind="bar",size=20)
plt.xlabel("Sub continent Divisions");
plt.ylabel("Percentage(%)")
plt.title("Renewable Energy consumption(% of final energy cosumption)");
fig.savefig('wbsdgace2.jpg',format='jpg');
infile.close();

##----------------- Intensity of primary Energy ------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

ped = [];
csd = ["Low income","Lower middle income","Upper middle income","High income","World"];

for row in csvdata:
    if (row[3]=="EG.EGY.PRIM.PP.KD"):
        if (row[0]==csd[0]):
            li=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[1]):
            lm=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[2]):
            um=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[3]):
            hi=[float(row[-27]),float(row[-5])];
        if (row[0]==csd[4]):
            wd=[float(row[-27]),float(row[-5])];
            wr = row;

ped = [li,lm,um,hi,wd];
outfile = open("temp.csv","w");
headerContent = "Divisions"+"," + "value"+"," + "year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(csd)):
    outfile.writelines(csd[i]+","+str(ped[i][0]) +","+"1990"+"\n");
    outfile.writelines(csd[i]+","+str(ped[i][1]) +","+"2012"+"\n");
outfile.close();

aeddata = pd.read_csv("temp.csv");

colorcodes = ["#e74c3c","#2e9971"];
sb.set_color_codes("muted");
sb.set_palette(colorcodes);
sb.set_context("poster");

plt.figure(figsize=(20,10),dpi=300)
fig=sb.factorplot(x="Divisions",y="value",hue="year",data=aeddata,kind="bar",size=12)
plt.xlabel("Income Type");
plt.ylabel(wr[2]);
plt.title(wr[2] +" Vs Income Category");
fig.savefig('wbsdgace3.jpg',format='jpg');
infile.close();