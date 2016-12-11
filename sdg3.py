# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:07:43 2016

@author: Deepak Kumar, 73217151
SDG: Gender Equality
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

def convToFloat(inputList):
    outputList = [];
    for i in range(0,len(inputList)):
        if(inputList[i]!=""):
            outputList.append(float(inputList[i]));
        else:
            outputList.append(0);
    return outputList;

##------------------------ Firm ownership and management----------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="IC.FRM.FEMO.ZS"):
        if (row[0]=="World"):
            fowr = float(row[-2]);

    if (row[3]=="IC.FRM.FEMM.ZS"):
        if (row[0]=="World"):
            fmwr = float(row[-2]);

mowr = 100-fowr;
mmwr = 100-fmwr;

fdata = [fowr,fmwr];
mdata = [mowr,mmwr];

sb.set_color_codes("muted");
sb.set_context("notebook",rc={"lines.linewidth":4.3})

fig = plt.figure(figsize=(10,10),dpi=300);
N=2;
ind = np.arange(N);
width = .8;
plt.bar(ind,fdata,width,label="Women",color='r');
plt.bar(ind,mdata,width,bottom=fdata,label="Men",color='b');
plt.ylabel("Percentage");
plt.title("Share of firms,2015");
plt.xticks(ind+width/2.0,("Firm ownership by sex","Firm top manager positions"))
plt.legend();
fig.savefig('wbsdgge1.jpg',format='jpg')
infile.close();

##-------------------- Young brides having more children--------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
ybd = [];

for row in csvdata:
    if row[3]=="SP.ADO.TFRT":
        if row[-3]!="":
            ybd.append([row[1],float(row[-3])]);

ybd.sort(key = lambda x:-x[1])

outfile = open("temp.csv","w");
headerContent = "Country"+"," + "value" + "\n";
outfile.writelines(headerContent);

for i in range(0,50):
    outfile.writelines(ybd[i][0]+","+str(ybd[i][1]) +"\n");       
outfile.close();

ybdata = pd.read_csv("temp.csv");
sb.set_color_codes("muted");
fig1=plt.figure(figsize=(10,20),dpi=300)
sb.barplot(x="value",y="Country",data=ybdata,color="b")
plt.title("Adolescent fertility rate, 2014 (births per 1,000 women ages 15-19)")
fig1.savefig('wbsdgge2.jpg',format='jpg');
infile.close();