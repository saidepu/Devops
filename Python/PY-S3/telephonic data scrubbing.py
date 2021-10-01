import os
import time
import csv

ignored = {'ScrubbingNORM'}
merge_list1 = []
path='C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome'
cust_list = [ item for item in os.listdir(path) if item not in ignored if os.path.isdir(os.path.join(path, item)) ]
for cust in cust_list:
    path1 = 'C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome/'+cust
    #get input file for each customer here
    #read the input file
    #convert to csv
    file_list = [ item for item in os.listdir(path1) if os.path.isfile(os.path.join(path1, item)) ]
    t = time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(path1)))
    print t
    print file_list
    file_list1 = ''.join(file_list)
    print file_list1
    f = open('C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome\ScrubbingNORM/'+str(file_list1),'w+')
    #enter normalized file csv conversion from original.csv logic here
    #read the normalized file
    #write it
    f.close()
    rename= cust+ '_'
    m = rename+str(file_list1)
    print m
    os.chdir('C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome\ScrubbingNORM/')
    os.rename('C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome\ScrubbingNORM/'+file_list1, 'C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome\ScrubbingNORM/'+m)
    merge_list = [cust] + [path1] + [file_list1] +[t]
    merge_list1.append(merge_list)
f1 = open('MetaData.txt','w+')
f2 = open('MetaData.txt','a')
f2.write('CustomerID,Path,Files,Time'+'\n')
f2.close()
for i in range(0, len(merge_list1)):
    print merge_list1[i]
    m2 = ''.join(str(merge_list1[i]))
    f3 = open('MetaData.txt','a')
    f3.write(m2+'\n')


for item in merge_list1:
    list1 = ''.join(item)
    #print (item[0],
#           item[1],
 #          item[2],
  #         item[3])
   # f = open('MetaData.txt','w+')
    #f.write(list1)
f3.close()

with open('MetaData.txt','rb') as file_comma1:
    with open('MetaData.csv','w+') as file_comma2:
        csv.writer(file_comma2, delimiter = ',').writerows(csv.reader(file_comma1, delimiter = ','))



   














    

