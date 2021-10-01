import schedule
import time

def job():
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
          print '\n'
        else:
          print "File is accepted! Please proceed!"
          print '\n'
        total = total + record_count
        if total > threshold:
          print "Threshold value exceeded! Please resubmit the files"
          print '\n'
        else:
          print "Records match within the threshold limit! Please proceed further!"
          print '\n'
    print "Total number of records: ", total

schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("9:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
