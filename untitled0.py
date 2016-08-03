# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 20:54:16 2016

@author: Enric
"""

import os

def t_(data):
    name=data[0]
    number=data[1]
    return name[0]+'_'+name[1:]+' = '+number
os.chdir('C:/Users/Enric/Documents/FSAE/Luis')
f=open('Tires clean csv.csv','r')
lines=f.readlines()
f.close()

clean_data=[]
to_skip=0
for i,line in enumerate(lines):
    if line[:4]=='Tire':
        #skip shitty lines
        to_skip=4
    elif line[:4]=='Phys':
        to_skip=1
    elif line[:4]=='2007':
        to_skip=7
    
    if to_skip==0:
        clean_data.append(line.strip().split(';'))
    else:
        to_skip-=1
        
data_in_blocks=[]
for i in range(len(clean_data[::30])):
    data_in_blocks.append(clean_data[i*30:i*30+30])
    
Fuckin_good=[]
for i,block in enumerate(data_in_blocks):
    #first shitty lines    
    shit='%=========================================================================='
    rows=[shit,"tireID = 'culo%02d'"%(i+1),shit,
          "% Physical Characteristics",shit]
          
    #get physical characcteristics
    rows.append(t_(block[0][0:2]))
    rows.append(t_(block[1][0:2]))
    rows.append(shit)
    rows.append("% Longitudinal Force--Pure Longitudinal Slip ")
    rows.append(shit)
    #get longitudinal force
    for row in range(3,17):
        rows.append(t_(block[row][0:2]))
    rows.append(shit)
    rows.append("% Lateral Force--Pure Side Slip")
    rows.append(shit)
    #get lateral force slip
    for row in range(0,18):
        rows.append(t_(block[row][2:4]))
    rows.append(shit)
    rows.append("% Aligning Torque")
    rows.append(shit)
    #get torkii
    for row in range(0,25):
        rows.append(t_(block[row][4:6]))
    rows.append(shit)
    rows.append("% Longitudinal Force--Combined Slip")
    rows.append(shit)
    #get longitudi, combined slip
    for row in range(18,22):
        rows.append(t_(block[row][0:2]))
    rows.append(shit)
    rows.append("% Lateral Force--Combined Slip")
    rows.append(shit)
    #get lateral combislip
    for row in range(20,30):
        rows.append(t_(block[row][2:4]))
        
    Fuckin_good.append(rows)
    filename=rows[1][10:16]+'.m'
    culo=open(filename,'w')
    for row in rows:
        culo.write(row+'\n')
    culo.close()



    