import csv 
'''
Utility function if any file consits of any NULL value.
'''
def mycsv_reader(csv_reader): 
  while True: 
    try: 
      yield next(csv_reader) 
    except csv.Error: 
      # error handling what you want.
      if '\0' in open(mycsv).read():
        print("have null byte")
      pass
    continue 
  return
     
if __name__ == '__main__': 
    reader = mycsv_reader(csv.reader(open('data.csv',encoding='utf-8')))
    for line in reader:
        print(line)