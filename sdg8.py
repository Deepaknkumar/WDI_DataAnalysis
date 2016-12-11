# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:14:34 2016

@author: Deepak Kumar, 73217151
SDG: Peace, justice and Strong Institutions
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

##------------------------------ International homicides --------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];
csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="VC.IHR.PSRC.P5"):
        if (row[0]==csd[0]):
            na = float(row[-5]);
        if (row[0]==csd[1]):
            eca=float(row[-5]);
        if (row[0]==csd[2]):
            lac=float(row[-5]);
        if (row[0]==csd[3]):
            mena=float(row[-5]);
        if (row[0]==csd[4]):
            eap=float(row[-5]);
        if (row[0]==csd[5]):
            sa=float(row[-5]);
        if (row[0]==csd[6]):
            ssa=float(row[-5]);
        if (row[0]==csd[7]):
            wd=float(row[-5]);
            wr = row;
            
aed = [na,eca,lac,mena,eap,sa,ssa,wd];

sb.set_color_codes("muted");
sb.set_context("poster");

fig = plt.figure(figsize=(25,25),dpi=300)
sb.barplot(csd,aed,color="b")
plt.xlabel("Landmasses")
plt.ylabel("Number")
plt.title("International Homicides, 2012 (per 100,000 people)");
fig.savefig('wbsdgpji1.jpg',format='jpg');
infile.close();

##------------------------- Battle related deaths -----------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

csd = ["Syrian Arab Republic","Afghanistan","Iraq","Ukraine","Nigeria","Pakistan","South Sudan","Israel","Yemen, Rep.","Somalia"];

for row in csvdata:
    if (row[3]=="VC.BTL.DETH"):
        if (row[0]==csd[0]):
            sar = float(row[-3]);
        if (row[0]==csd[1]):
            af=float(row[-3]);
        if (row[0]==csd[2]):
            iraq=float(row[-3]);
        if (row[0]==csd[3]):
            ukr=float(row[-3]);
        if (row[0]==csd[4]):
            nig=float(row[-3]);
        if (row[0]==csd[5]):
            pak=float(row[-3]);
        if (row[0]==csd[6]):
            ssu=float(row[-3]);
        if (row[0]==csd[7]):
            isr=float(row[-3]);
        if (row[0]==csd[8]):
            yp=float(row[-3]);
        if (row[0]==csd[9]):
            som=float(row[-3]);
                      
aed = [sar,af,iraq,ukr,nig,pak,ssu,isr,yp,som];

sb.set_color_codes("muted");
sb.set_context("poster");

fig = plt.figure(figsize=(25,25),dpi=300)
sb.barplot(aed,csd,color="b")
plt.ylabel("Countries")
plt.title("Battle related deaths, 2014");
fig.savefig('wbsdgpji2.jpg',format='jpg');
infile.close();

##------------------------- Registered under age 5 children ------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

csd = ["Europe & Central Asia","Latin America & Caribbean","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if (row[3]=="SP.REG.BRTH.ZS"):
        if (row[0]==csd[0]):
            eca = float(row[-4]);
        if (row[0]==csd[1]):
            lac=float(row[-4]);
        if (row[0]==csd[2]):
            sa=float(row[-4]);
        if (row[0]==csd[3]):
            ssa=float(row[-4]);
        if (row[0]==csd[4]):
            wd=float(row[-4]);
            wr = row;
                      
aed = [eca,lac,sa,ssa,wd];

sb.set_color_codes("muted");
sb.set_context("poster");

fig = plt.figure(figsize=(25,25),dpi=300)
sb.barplot(csd,aed,color="b")
plt.title(wr[2] +" ,2013");
fig.savefig('wbsdgpji3.jpg',format='jpg');
infile.close();