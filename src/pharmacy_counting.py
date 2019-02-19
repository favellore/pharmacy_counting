#!/usr/bin/python
# -*- coding: utf-8 -*-
# Open file with .txt as input
with open ('input/itcont.txt','r') as input:
    line = input.readline().replace('\n','')
    drug_name=[]
    drug_cost=[]
    while line:
# seperate the file with commas (,)
        line = input.readline().replace('\n','')
        words=line.split(',')
# The thrid colum is the drug name in the input file so appending the words to get a full list
# Also, the last column [4] has cost part, however, there are some data which is not cleaned
# and missing values, which makes [4] not exist, so [-1] which tooks last column help this issue
        try:
            drug_name.append(words[3])
        except:
            continue
        try:
            drug_cost.append(float(words[-1]))
        except:
            drug_cost.append(0)
            print('Invalid Drug cost for line %s /n', line)
            
# The dict below drug_summary will create an arthemetic assignment to add drug cost and count
    drug_summary={}
    for i, name in enumerate(drug_name):
        if name in drug_summary.keys():
            drug_summary [name][0]+=1
            drug_summary [name][1]+=drug_cost[i]
        else:
            drug_summary[name]=[0,0]
            drug_summary[name][0]=1
            drug_summary[name][1]=drug_cost[i]
# Sorting the data
        drug_summary_sorted = sorted(drug_summary.items(), key=lambda x:x[0])
        drug_summary_sorted = sorted(drug_summary_sorted, key=lambda x:x[1][1], reverse = True)
# Below code will open a txt file as "top_cost_drug.txt and write the output
# This file is present in output folder
drugs=open("output/top_cost_drug.txt","w")    
print("drug_name,num_prescriber,total_cost",file=drugs)
# Thcode below will actuall write all the required top drugs seperated by comma(,)
for item in drug_summary_sorted:
    print(item[0],str(item[1][0]),((int(item[1][1]))),sep=',',file=drugs)
drugs.close()
