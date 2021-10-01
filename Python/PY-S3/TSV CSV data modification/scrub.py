import os

ignored = {'ScrubbingNORM'}
path='C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome'
cust_list = [ item for item in os.listdir(path) if item not in ignored if os.path.isdir(os.path.join(path, item)) ]
for cust in cust_list:
    #Get all the customers
    #print cust
    cust_path = os.path.join(path, cust)
    print cust_path
    cust_file = os.listdir(cust_path)
    print cust_file
    norm_path = 'C:\Users\srinivasanravi\Desktop\python\cluster\stc2\myhome\ScrubbingNORM'
    norm_list = [ item for item in os.listdir(norm_path) if os.path.isfile(os.path.join(norm_path, item)) ]
    for norm in norm_list:
       print norm
       if norm in cust_file == True
           print cust_file
       else:
           print "no"
    
     
