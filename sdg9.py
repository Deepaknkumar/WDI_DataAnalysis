# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:55:19 2016

@author: Deepak Kumar, 73217151
SDG: Life below water
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

##-------------------- Marine Protected Areas --------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];

csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="ER.MRN.PTMR.ZS"):
        if (row[0]==csd[0]):
            na=[float(row[-27]),float(row[-3])];
        if (row[0]==csd[1]):
            eca=[float(row[-27]),float(row[-3])];
        if (row[0]==csd[2]):
            lac=[float(row[-27]),float(row[-3])];
        if (row[0]==csd[3]):
            mena=[float(row[-27]),float(row[-3])];
        if (row[0]==csd[4]):
            eap=[float(row[-27]),float(row[-3])];
        if (row[0]==csd[5]):
            sa=[float(row[-27]),float(row[-3])];
        if (row[0]==csd[6]):
            ssa=[float(row[-27]),float(row[-3])];
        if (row[0]==csd[7]):
            wd=[float(row[-27]),float(row[-3])];
            wr = row;

aed = [na,eca,lac,mena,eap,sa,ssa,wd];
outfile = open("temp.csv","w");
headerContent = "Landmasses"+"," + "value"+"," + "year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(csd)):
    outfile.writelines(csd[i]+","+str(aed[i][0]) +","+"1990"+"\n");
    outfile.writelines(csd[i]+","+str(aed[i][1]) +","+"2014"+"\n");
outfile.close();

aeddata = pd.read_csv("temp.csv");

colorcodes = ["#e74c3c","#2e9971"];
sb.set_color_codes("muted");
sb.set_palette(colorcodes);
sb.set_context("poster");

plt.figure(figsize=(20,10),dpi=300)
fig=sb.factorplot(x="Landmasses",y="value",hue="year",data=aeddata,kind="bar",size=20)
plt.xlabel("Landmasses");
plt.ylabel(wr[2])
plt.title(wr[2]+ " in different areas of world");
fig.savefig('wbsdglbw1.jpg',format='jpg');
infile.close();

