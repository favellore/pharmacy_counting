

# InsightDataScience/pharmacy_counting

## Table of Content

1) Problem
2) Input Dataset
3) Approach
4) Run


## Problem

This Python script is used to analyse the pharmacy data to generate a list of drugs, the total number of UNIQUE individials who prescribed the medication, and the total drug cost, which must be listed in descending order.

Insight DataScience asked to tackle this challenge without using the libraries. Thats a challenge if we are used to have libraries in our daily usage. However, to test the knowledge of basics of Python, this is a good start.


## Input Dataset

* [Click here to download full dataset as provided in Challenge](https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view) -Its a large dataset containing over 24 million records. Note, we will use it to test the full functionality of your code, along with other tests.

The input folder has the folder 

```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500

```
then output file will have the following output
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300

```
## Approach

Tackling the problem 

* Without using the library imported the text file , for this problem we run a small file, however the same code could be used to tackle large file. The processing time will be increased to two to three minutes.
* Seperate the file with commas and read line by line
* There should be five columns in the file, some rows has less than five columns, this is takled by using [-1]
* Append the list
* Create a dict. to perform arthemetic operations
* Open a txt file
* Write the required output


##Run


```

./run.sh


```








