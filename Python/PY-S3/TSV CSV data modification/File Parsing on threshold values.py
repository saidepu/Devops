allfiles = 'Files.txt'
with open(allfiles) as A:
 total = 0
 threshold = 20
 for line in A:
    line1 = line.strip('\n')
    f = line1 + '.txt'
    print f
    record_count = sum(1 for line in open(f))
    print record_count 
    if record_count > threshold:
       print "File is rejected! Please submit the file in chunks or resubmit it"
       record_count = 0
       #Send response as FAIL here
       print '\n'
    else:
       print "File is accepted! Please proceed!"
       #Send response as PASS here
       print '\n'
    total = total + record_count
    if total > threshold:
       print "Threshold value exceeded! Please resubmit the files"
       #Send response as FAIL here
       print '\n'
    else:
       print "Records match within the threshold limit! Please proceed further!"
       #Send response as PASS here
       print '\n'
 print "Total number of records: ", total
