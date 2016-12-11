# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Deepak Kumar, 73217151
SDG: Good health and Well Being
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

#indicators = pd.read_csv('WDI_Data.csv');
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

##------------------------ Maternal Mortality ratio(per 100,000 live births)----------
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
    if (row[3]=="SH.STA.MMRT") and (row[0]=="World"):
        wr = row;
    if (row[3]=="SH.STA.MMRT") and (row[0]=="Sub-Saharan Africa"):
        ssar = row;
    if (row[3]=="SH.STA.MMRT") and (row[0]=="South Asia"):
        sar = row;
    if (row[3]=="SH.STA.MMRT") and (row[0]=="Middle East & North Africa"):
        menar = row;
    if (row[3]=="SH.STA.MMRT") and (row[0]=="Europe & Central Asia"):
        ecar = row;
    if (row[3]=="SH.STA.MMRT") and (row[0]=="East Asia & Pacific"):
        eapr = row;
    if (row[3]=="SH.STA.MMRT") and (row[0]=="High income"):
        hir = row;
    if (row[3]=="SH.STA.MMRT") and (row[0]=="Latin America & Caribbean"):
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
fig.savefig('wbsdgghwb1.jpg',format='jpg')
infile.close();

##-------------- Adolescent fertility rate -----------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wy = [];
wd = [];
li = [];
lm = [];
um = [];
hi = [];

for row in csvdata:
    if (row[3]=="SP.ADO.TFRT"):
        if (row[0]=="World"):
            wr = row;
        if (row[0]=="Lower middle income"):
            lmr = row;
        if (row[0]=="Low income"):
            lir = row;
        if (row[0]=="Upper middle income"):
            umr = row;
        if (row[0]=="High income"):
            hir = row;

for i in range(4,len(wr)):
    if(wr[i] !="") and (lmr[i]!="") and (lir[i]!="") and (umr[i]!="") and (hir[i]!=""):
        wy.append(headersData[i]);
        wd.append(float(wr[i]));
        lm.append(float(lmr[i]));
        li.append(float(lir[i]));
        um.append(float(umr[i]));
        hi.append(float(hir[i]));
                        
sb.set_palette("colorblind")
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(20,10),dpi=300);
plt.plot(wy,wd,label="World Data")
plt.plot(wy,lm,label="Lower middle income")
plt.plot(wy,li,label="Low income")
plt.plot(wy,um,label="Upper middle income")
plt.plot(wy,hi,label="High Income")
plt.xlabel("Years")
plt.ylabel(wr[2])
plt.legend();
plt.title(wr[2] + "Vs Years")
fig.savefig('wbsdgghwb2.jpg',format='jpg')
infile.close();

##------------- under five mortality rate -----------------------------------
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
    if (row[3]=="SH.DYN.MORT"):
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

                         
sb.set_palette("Set1")
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
fig.savefig('wbsdgghwb3.jpg',format='jpg')
infile.close();

##---------- Mortality coused by traffic Injury --------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wy = [];
wd = [];
li = [];
lm = [];
um = [];
hi = [];

for row in csvdata:
    if (row[3]=="SH.STA.TRAF.P5"):
        if (row[0]=="World"):
            wr = row;
        if (row[0]=="Lower middle income"):
            lmr = row;
        if (row[0]=="Low income"):
            lir = row;
        if (row[0]=="Upper middle income"):
            umr = row;
        if (row[0]=="High income"):
            hir = row;

for i in range(4,len(wr)):
    if(headersData[i]=="2013"):
        wd=float(wr[i]);
        lm=float(lmr[i]);
        li=float(lir[i]);
        um=float(umr[i]);
        hi=float(hir[i]);
                        
sb.set_style("darkgrid")
sb.set_context("notebook",rc={"lines.linewidth":2.3})

fig = plt.figure(figsize=(20,10),dpi=300);
xdata = ["Low income", "Lower middle income", "Upper middle income", "High income", "World"];
ydata = [li,lm,um,hi,wd];
sb.barplot(xdata,ydata)
plt.xlabel("Years")
plt.ylabel(wr[2])
plt.legend();
plt.title(wr[2] + " in 2013")
fig.savefig('wbsdgghwb4.jpg',format='jpg')
infile.close();