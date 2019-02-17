with open ('de_cc_data.txt','r') as input:
    line = input.readline().replace('\n','')

    drug_name=[]
    drug_cost=[]
    while line:
        line = input.readline().replace('\n','')
        words=line.split(',')
        try:
            drug_name.append(words[3])
        except:
            continue
        try:
            drug_cost.append(float(words[-1]))
        except:
            drug_cost.append(0)
            print('incorrect drug cost for line %s /n', line)
    drug_summary={}
    for i, name in enumerate(drug_name):
        if name in drug_summary.keys():
            drug_summary [name][0]+=1
            drug_summary [name][1]+=drug_cost[i]
        else:
            drug_summary[name]=[0,0]
            drug_summary[name][0]=1
            drug_summary[name][1]=drug_cost[i]
            
        drug_summary_sorted = sorted(drug_summary.items(), key=lambda x:x[0])
        drug_summary_sorted = sorted(drug_summary_sorted, key=lambda x:x[1][1], reverse = True)
        
top_cost_drug=open("top_cost_drug.txt","w")    
print("drug_name,num_prescriber,total_cost",file=state)
for item in drug_summary_sorted:
    print(item[0],str(item[1][0]),((int(item[1][1]))),sep=',',file=top_cost_drug)

top_cost_drug.close()
