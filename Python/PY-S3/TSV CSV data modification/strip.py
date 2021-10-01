import pandas as pd
import csv
import os

#converting output pipe delimited file to an intermediate csv format
#with open('output.txt','rb') as file_pipe:
    #with open('output.csv','wb') as file_comma:
       # csv.writer(file_comma, delimiter = ',').writerows(csv.reader(file_pipe, delimiter = '|'))
       # dfoutput = pd.read_csv('output.csv', header = None)


#ignored = {'scrubing'}
path='C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome'
cust_list = [ item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) ]
for cust1 in cust_list:
 paath ='C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome/' +cust1
 file_list = [ item for item in os.listdir(paath) if os.path.isdir(os.path.join(paath, item))]
 for file in file_list:
   with open(file,'rb') as file_pipe1:
    with open('file.csv','wb') as file_comma1:
     csv.writer(file_comma1, delimiter = ',').writerows(csv.reader(file_pipe1, delimiter = '|'))
     dfinput1 = pd.read_csv('file.csv', header = None)
     dfop1 = []
     for cols1 in dfinput1:
      if dfinput1[cols1].map(str).apply(len).eq(10).any() == True:
       dfreqA = dfinput1[cols1]
       if dfinput1[cols1].map(str).apply(len).eq(8).any() == True:
        dfreqB = dfinput1[cols1]
        if dfinput1[cols1].map(str).apply(len).eq(10).any() == False and  dfinput1[cols1].map(str).apply(len).eq(8).any() == False:
         dfop1.append(dfinput1[cols1])
         dfrequired1 = pd.concat([dfreqA, dfreqB], axis = 1)
         dfop1 = pd.concat(dfop1, axis = 1)
         df1 = pd.read_csv('file.csv', header = None)
         dfoutput_2 = pd.read_csv('file.csv', header = None)
         del dfoutput_2
         dfoutput_3 = pd.read_csv('file.csv', header = None)
         dfoutput_3.to_csv('file.csv', header = None, index = False)
         results1 = pd.concat([dfrequired1, dfop1], axis = 1)
         results1.to_csv('file.csv', header = None, index = False)

#converting normalized csv file to normalized pipe delimited format
         with open('file.csv','rb') as file_comma3:
          with open(file,'wb') as file_pipe3:
           csv.writer(file_pipe3, delimiter = '|').writerows(csv.reader(file_comma3, delimiter = ','))


#Read original csv file and concatenate proper data to output csv file before conversion  
          dfinput = pd.read_csv('file.csv', header = None)
          dfop = []
          for cols1 in dfinput:
           if dfinput[cols1].map(str).apply(len).eq(10).any() == True:
            dfreq1 = dfinput[cols1]
            if dfinput[cols1].map(str).apply(len).eq(8).any() == True:
             dfreq2 = dfinput[cols1]
             if dfinput[cols1].map(str).apply(len).eq(10).any() == False and  dfinput[cols1].map(str).apply(len).eq(8).any() == False:
              dfop.append(dfinput[cols1])
              dfrequired = pd.concat([dfreq1, dfreq2], axis = 1)
              dfop = pd.concat(dfop, axis = 1)

              df = pd.read_csv('file.csv', header = None)
              dfoutput_1 = pd.read_csv('file.csv', header = None)
              del dfoutput_1
              dfoutput_2 = pd.read_csv('file.csv', header = None)
              dfoutput_2.to_csv('file.csv', header = None, index = False)
              results = pd.concat([dfrequired, dfoutput, dfop], axis = 1)
              results.to_csv('file.csv', header = None, index = False)

#converting output csv file to pipe delimited format
              with open('file.csv','rb') as file_comma2:
               with open(file,'wb') as file_pipe2:
                csv.writer(file_pipe2, delimiter = '|').writerows(csv.reader(file_comma2, delimiter = ','))

