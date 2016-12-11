# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:55:19 2016

@author: Deepak Kumar, 73217151
SDG: Life on land
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import csv

##-------------------- Change in Forest areas, 1990-2015 --------------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);
wc = 0;
headersData = [];

csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if(wc==0):
        headersData = row;
        wc=wc+1;
    if (row[3]=="AG.LND.FRST.K2"):
        if (row[0]==csd[0]):
            na=-float(row[-27])+float(row[-2]);
        if (row[0]==csd[1]):
            eca=-float(row[-27])+float(row[-2]);
        if (row[0]==csd[2]):
            lac=-float(row[-27])+float(row[-2]);
        if (row[0]==csd[3]):
            mena=-float(row[-27])+float(row[-2]);
        if (row[0]==csd[4]):
            eap=-float(row[-27])+float(row[-2]);
        if (row[0]==csd[5]):
            sa=-float(row[-27])+float(row[-2]);
        if (row[0]==csd[6]):
            ssa=-float(row[-27])+float(row[-2]);
        if (row[0]==csd[7]):
            wd=-float(row[-27])+float(row[-2]);
            wr = row;

aed = [na,eca,lac,mena,eap,sa,ssa,wd];
"""outfile = open("temp.csv","w");
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
"""
fig = plt.figure(figsize=(25,25),dpi=300)
sb.barplot(csd,aed,color="b")
plt.xlabel("Landmasses")
plt.ylabel("hectares")
plt.title("Change in forest area,1990-2015");
fig.savefig('wbsdglol1.jpg',format='jpg');
infile.close();

##------------------------ National Protected Area ----------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if (row[3]=="ER.LND.PTLD.ZS"):
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
headerContent = "Divisions"+"," + "value"+"," + "year"+"\n";
outfile.writelines(headerContent);

for i in range(0,len(csd)):
    outfile.writelines(csd[i]+","+str(aed[i][0]) +","+"1990"+"\n");
    outfile.writelines(csd[i]+","+str(aed[i][1]) +","+"2014"+"\n");
outfile.close();

aeddata = pd.read_csv("temp.csv");

colorcodes = ["#e74c3c","#2e9971"];
sb.set_color_codes("bright");
sb.set_palette(colorcodes);
sb.set_context("poster")

plt.figure(figsize=(20,15),dpi=300)
fig=sb.factorplot(x="Divisions",y="value",hue="year",data=aeddata,kind="bar",size=20)
plt.xlabel("Landmasses");
plt.ylabel(wr[2])
plt.title(wr[2]+ " in different areas of world");
fig.savefig('wbsdglol2.jpg',format='jpg');
infile.close();

##------------------------ Threatened species 2015 ----------------------------
infile = open('WDI_Data.csv','r');
csvdata = csv.reader(infile);

csd = ["North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"];

for row in csvdata:
    if (row[3]=="EN.MAM.THRD.NO"):
        if (row[0]==csd[0]):
            mna=float(row[-1]);
        if (row[0]==csd[1]):
            meca=float(row[-1]);
        if (row[0]==csd[2]):
            mlac=float(row[-1]);
        if (row[0]==csd[3]):
            mmena=float(row[-1]);
        if (row[0]==csd[4]):
            meap=float(row[-1]);
        if (row[0]==csd[5]):
            msa=float(row[-1]);
        if (row[0]==csd[6]):
            mssa=float(row[-1]);
        if (row[0]==csd[7]):
            mwd=float(row[-1]);
    if (row[3]=="EN.BIR.THRD.NO"):
        if (row[0]==csd[0]):
            bna=float(row[-1]);
        if (row[0]==csd[1]):
            beca=float(row[-1]);
        if (row[0]==csd[2]):
            blac=float(row[-1]);
        if (row[0]==csd[3]):
            bmena=float(row[-1]);
        if (row[0]==csd[4]):
            beap=float(row[-1]);
        if (row[0]==csd[5]):
            bsa=float(row[-1]);
        if (row[0]==csd[6]):
            bssa=float(row[-1]);
        if (row[0]==csd[7]):
            bwd=float(row[-1]);
    if (row[3]=="EN.FSH.THRD.NO"):
        if (row[0]==csd[0]):
            fna=float(row[-1]);
        if (row[0]==csd[1]):
            feca=float(row[-1]);
        if (row[0]==csd[2]):
            flac=float(row[-1]);
        if (row[0]==csd[3]):
            fmena=float(row[-1]);
        if (row[0]==csd[4]):
            feap=float(row[-1]);
        if (row[0]==csd[5]):
            fsa=float(row[-1]);
        if (row[0]==csd[6]):
            fssa=float(row[-1]);
        if (row[0]==csd[7]):
            fwd=float(row[-1]);
    if (row[3]=="EN.HPT.THRD.NO"):
        if (row[0]==csd[0]):
            pna=float(row[-1]);
        if (row[0]==csd[1]):
            peca=float(row[-1]);
        if (row[0]==csd[2]):
            plac=float(row[-1]);
        if (row[0]==csd[3]):
            pmena=float(row[-1]);
        if (row[0]==csd[4]):
            peap=float(row[-1]);
        if (row[0]==csd[5]):
            psa=float(row[-1]);
        if (row[0]==csd[6]):
            pssa=float(row[-1]);
        if (row[0]==csd[7]):
            pwd=float(row[-1]);
                      
paed = [pna,peca,plac,pmena,peap,psa,pssa,pwd];
maed = [mna,meca,mlac,mmena,meap,msa,mssa,mwd];
bfaed = [mna+pna,meca+peca,plac+mlac,pmena+mmena,peap+meap,psa+msa,pssa+mssa,pwd+mwd];
faed = [fna,feca,flac,fmena,feap,fsa,fssa,fwd];
bbaed = [fna+bfaed[0],feca+bfaed[1],flac+bfaed[2],fmena+bfaed[3],feap+bfaed[4],fsa+bfaed[5],fssa+bfaed[6],fwd+bfaed[7]];
baed = [bna,beca,blac,bmena,beap,bsa,bssa,bwd];

#colorcodes = ["#e74c3c","#2e9971"];
#sb.set_color_codes("bright");
#sb.set_palette(colorcodes);
sb.set_context("poster")

sb.set_color_codes("muted");
#sb.set_context("notebook",rc={"lines.linewidth":4.3})
sb.set_context("poster");

fig = plt.figure(figsize=(25,17),dpi=300);
ind = np.arange(len(paed));
width = .8;
plt.bar(ind,paed,width,label="Plants",color='b');
plt.bar(ind,maed,width,bottom=paed,label="Mammals",color='k');
plt.bar(ind,faed,width,bottom=bfaed,label="Fish",color="r")
plt.bar(ind,baed,width,bottom=bbaed,label="Birds",color="g")
plt.ylabel("Number");
plt.title("Number of threatened species,2016");
plt.xticks(ind+width/2.0,("North America","Europe & Central Asia","Latin America & Caribbean","Middle East & North Africa","East Asia & Pacific","South Asia","Sub-Saharan Africa","World"))
plt.legend();
fig.savefig('wbsdglol3.jpg',format='jpg')
infile.close();