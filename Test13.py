import csv

with open("cities.csv", "r") as f:
    csvreader = csv.reader(f)
    # for line in f.readline():
    #     if "Ravenn" in line:
    #         print(line)
    for row in csvreader:
        print(row[0], row[4])
        print()
        print(row)
        print()



 #EJEMPLO
#  # Python program to read CSV file line by line
# # import necessary packages
# import csv
  
# # Open file 
# with open('samplecsv.csv') as file_obj:
      
#     # Create reader object by passing the file 
#     # object to reader method
#     reader_obj = csv.reader(file_obj)
      
#     # Iterate over each row in the csv 
#     # file using reader object
#     for row in reader_obj:
#         print(row)