# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:22:39 2016

@author: Deepak Kumar, 73217151
SDG: Quality Education
"""
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

##------------------------ Maternal Mortality ratio(per 100,000 live births)----------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];

wy = [];
wd = [];
ssa = [];
sa = [];
mena = [];
eca = [];
eap = [];
hi = [];
lac = [];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="SE.PRM.CMPT.ZS"):
        if (row[0]=="World"):
            wr = row;
        if (row[0]=="Sub-Saharan Africa"):
            ssar = row;
        if (row[0]=="South Asia"):
            sar = row;
        if (row[0]=="Middle East & North Africa"):
            menar = row;
        if (row[0]=="Europe & Central Asia"):
            ecar = row;
        if (row[0]=="East Asia & Pacific"):
            eapr = row;
        if (row[0]=="High income"):
            hir = row;
        if (row[0]=="Latin America & Caribbean"):
            lacr = row;

for i in range(4,len(wr)):
    if(wr[i] !="") and (ssar[i]!="") and (sar[i]!="") and (menar[i]!="") and (ecar[i]!="") and (eapr[i]!="") and (hir[i]!="") and (lacr[i]!=""):
        wy.append(headersData[i]);
        wd.append(float(wr[i]));
        ssa.append(float(ssar[i]));
        sa.append(float(sar[i]));
        mena.append(float(menar[i]));
        eca.append(float(ecar[i]));
        eap.append(float(eapr[i]));
        hi.append(float(hir[i]));
        lac.append(float(lacr[i]));

                         
sb.set_palette("bright")
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(20,10),dpi=300);
plt.plot(wy,wd,label="World Data")
plt.plot(wy,ssa,label="Sub-Saharan Africa")
plt.plot(wy,sa,label="South Asia")
plt.plot(wy,mena,label="Middle East and North Africa")
plt.plot(wy,eca,label="Europe and Central Asia")
plt.plot(wy,eap,label="East Asia and Pacific")
sb.set_context("notebook",rc={"lines.linewidth":2.7})
plt.plot(wy,hi,label="High Income")
plt.plot(wy,lac,label="Latin America & Caribbean")
plt.xlabel("Years")
plt.ylabel(wr[2])
plt.legend();
plt.title(wr[2] + "Vs Years")
fig.savefig('wbsdgqe1.jpg',format='jpg')
infile.close();

##---------- Primary school age children out of school(Area Chart)-------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

wy = [];
wd = [];
ssa = [];
sa = [];
mena = [];
eca = [];
eap = [];
hi = [];
lac = [];

for row in csvdata:
    if (row[3]=="SE.PRM.UNER"):
        if (row[0]=="World"):
            wr = row;
        if (row[0]=="Sub-Saharan Africa"):
            ssar = row;
        if (row[0]=="South Asia"):
            sar = row;
        if (row[0]=="Middle East & North Africa"):
            menar = row;
        if (row[0]=="Europe & Central Asia"):
            ecar = row;
        if (row[0]=="East Asia & Pacific"):
            eapr = row;
        if (row[0]=="High income"):
            hir = row;
        if (row[0]=="Latin America & Caribbean"):
            lacr = row;

for i in range(4,len(wr)):
    if(wr[i] !="") and (ssar[i]!="") and (sar[i]!="") and (menar[i]!="") and (ecar[i]!="") and (eapr[i]!="") and (hir[i]!="") and (lacr[i]!=""):
        wy.append(headersData[i]);
        wd.append(float(wr[i]));
        ssa.append(float(ssar[i]));
        sa.append(float(sar[i]));
        mena.append(float(menar[i]));
        eca.append(float(ecar[i]));
        eap.append(float(eapr[i]));
        hi.append(float(hir[i]));
        lac.append(float(lacr[i]));

                         
sb.set_palette("muted")
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(20,10),dpi=300);
plt.plot(wy,wd,label="World Data")
plt.plot(wy,ssa,label="Sub-Saharan Africa")
plt.plot(wy,sa,label="South Asia")
plt.plot(wy,mena,label="Middle East and North Africa")
plt.plot(wy,eca,label="Europe and Central Asia")
plt.plot(wy,eap,label="East Asia and Pacific")
sb.set_context("notebook",rc={"lines.linewidth":2.7})
plt.plot(wy,hi,label="High Income")
plt.plot(wy,lac,label="Latin America & Caribbean")
plt.xlabel("Years")
plt.ylabel(wr[2])
plt.legend();
plt.title(wr[2] + "Vs Years")
fig.savefig('wbsdgqe2.jpg',format='jpg')
infile.close();

##------------------------------------- Gross enrollment pre-primary-----------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
cf = ["Low income","Lower middle income","Upper middle income","High income"];
cl = [];
wy = [];

for row in csvdata:
    if (row[3]=="SE.PRE.ENRR"):
        if (row[0]=="Lower middle income"):
            lmr = row;
        if (row[0]=="Low income"):
            lir = row;
        if (row[0]=="Upper middle income"):
            umr = row;
        if (row[0]=="High income"):
            hir = row;

for i in range(4,len(wr)):
    if(lir[i] !="") and (lmr[i]!="") and (umr[i]!="") and (hir[i]!="") and ((headersData[i]=="1990") or (headersData[i]=="2012")):
        wy.append(headersData[i]);
        cl.append([float(lir[i]),float(lmr[i]),float(umr[i]),float(hir[i])]);

outfile = open("temp.csv","w");
headerContent = "Income Type"+"," + "value" + "," +"year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(cf)):
    outfile.writelines(cf[i]+","+str(cl[0][i])+","+wy[0] +"\n");
    outfile.writelines(cf[i]+","+str(cl[1][i])+","+wy[1] +"\n");

outfile.close();

comdata = pd.read_csv("temp.csv");

sb.set_palette("Set1");
sb.set_context("notebook");
fig = sb.factorplot(x="Income Type", y="value", hue="year", data=comdata,size=10, kind="bar",aspect=1);
plt.title("Pre-primary");
plt.ylabel("Gross enrollment ratio(%)");
fig.savefig('wbsdgqe3.jpg',format='jpg')
infile.close();

##--------------------------- Gross Enrollment tertiary ---------------------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
cf = ["Low income","Lower middle income","Upper middle income","High income"];
cl = [];
wy = [];

for row in csvdata:
    if (row[3]=="SE.TER.ENRR"):
        if (row[0]=="Lower middle income"):
            lmr = row;
        if (row[0]=="Low income"):
            lir = row;
        if (row[0]=="Upper middle income"):
            umr = row;
        if (row[0]=="High income"):
            hir = row;

for i in range(4,len(wr)):
    if(lir[i] !="") and (lmr[i]!="") and (umr[i]!="") and (hir[i]!="") and ((headersData[i]=="1990") or (headersData[i]=="2012")):
        wy.append(headersData[i]);
        cl.append([float(lir[i]),float(lmr[i]),float(umr[i]),float(hir[i])]);

outfile = open("temp.csv","w");
headerContent = "Income Type"+"," + "value" + "," +"year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(cf)):
    outfile.writelines(cf[i]+","+str(cl[0][i])+","+wy[0] +"\n");
    outfile.writelines(cf[i]+","+str(cl[1][i])+","+wy[1] +"\n");

outfile.close();

comdata = pd.read_csv("temp.csv");

sb.set_palette("muted");
sb.set_context("notebook");
fig = sb.factorplot(x="Income Type", y="value", hue="year", data=comdata,size=10, kind="bar",aspect=1);
plt.title("Tertiary");
plt.ylabel("Gross enrollment ratio(%)");
fig.savefig('wbsdgqe4.jpg',format='jpg')
infile.close();