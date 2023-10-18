import csv
import sys



try:
    fp_txt = open("source\data.txt")
except FileNotFoundError:
    print("File not found in source folder. Pleasae check again")
    sys.exit(1)






txt_data = fp_txt.readlines()


# print(type(txt_data[1]))

fo_txt = open("destination\daily_text.csv","a")

# if its a contact => it will start with a number and length will be 10
# if its an email then will have '@' as a letter

for item in txt_data:
    line_data = item.split(' ')
    for item2 in line_data:
        if '@' in item2:
            fo_txt.write(item2+'\n')
        elif len(item2) == 10:
            if item2.isnumeric():
                fo_txt.write(item2+'\n')

fp_txt.close()
fo_txt.close()

keys =['id','name','salary','city']
columns = [1,2,3,4]


with open("destination\daily_CSV.csv", "w") as fo_csv:
    writer = csv.DictWriter(fo_csv,keys)
    writer.writeheader()

    try:
        with open("source\data.csv", 'r') as fp_csv:
            reader = csv.DictReader(fp_csv)
            for row in reader:

                writer.writerow({'id':row['id'], 'name':row['name'], 'salary':row['salary'],'city':row['city']})

    except FileNotFoundError:
        print("File not found in source folder, please check again")
        sys.exit(2)


processed_txt = open("processed\daily_text_date_time.csv","w")
destination_txt = open("destination\daily_text.csv")

destination_data = destination_txt.read()

processed_txt.write(destination_data)

processed_txt.close()
destination_txt.close()




processed_csv = open("processed\daily_CSV_date_time.csv","w")
destination_csv = open("destination\daily_CSV.csv")

destination_CSV_data = destination_csv.read()
processed_csv.write(destination_CSV_data)

processed_csv.close()
destination_csv.close()
























