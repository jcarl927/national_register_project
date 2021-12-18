import csv
import pprint
from datetime import datetime

count_by_state = {}
count_by_category = {}
count_by_area_of_significance = {}
count_by_year_listed = {}

pp = pprint.PrettyPrinter(indent=4)

#create counters for properties by state, category, area of significance, and year listed
with open("/Users/juliecarlson/Desktop/628 Final Project/results/2021-11-01_National-Register-Processed-Dataset.csv", "r") as originalcsvfile:
    reader = csv.DictReader(originalcsvfile)
    for row in reader:
        #count number of properties by state
        if row['State'] not in count_by_state:
            count_by_state[row['State']]=0
        count_by_state[row['State']]=count_by_state[row['State']]+1
        #count number of properties by category, filtering out properties without a category
        if row['Category of Property'] != '':
            if row['Category of Property'] not in count_by_category:
                count_by_category[row['Category of Property']]=0
            count_by_category[row['Category of Property']]=count_by_category[row['Category of Property']]+1
        #count number of properties by area of significance, filtering out properties without an area of significance    
        if row['Area of Significance'] != '':
            #loop through rows that contain only one area of significance
            if ";" not in row['Area of Significance']:
                if row['Area of Significance'] not in count_by_area_of_significance:
                    count_by_area_of_significance[row['Area of Significance']]=0
                count_by_area_of_significance[row['Area of Significance']]=count_by_area_of_significance[row['Area of Significance']]+1
            #loop through rows that contain multiple areas of significance
            if ";" in row['Area of Significance']:
                area_of_signifiance_lists = row['Area of Significance'].split("; ")
                for row['Area of Significance'] in area_of_signifiance_lists:
                    if row['Area of Significance'] not in count_by_area_of_significance:
                        count_by_area_of_significance[row['Area of Significance']]=0
                    if row['Area of Significance'] in count_by_area_of_significance:
                        count_by_area_of_significance[row['Area of Significance']]=count_by_area_of_significance[row['Area of Significance']]+1
        #count the number of properties by the year they were added to the National Register
        if row['Listed Year'] != '':
            if row['Listed Year'] not in count_by_year_listed:
                count_by_year_listed[row['Listed Year']]=0
            count_by_year_listed[row['Listed Year']]=count_by_year_listed[row['Listed Year']]+1

#print dictionaries to check that the script has worked
pp.pprint(count_by_state)
pp.pprint(count_by_category)
pp.pprint(count_by_area_of_significance)
pp.pprint(count_by_year_listed)

#create csv file names that will include the date in ISO 8601 format
datestr = datetime.now().strftime("%Y-%m-%d")
count_by_state_file = "/Users/juliecarlson/Desktop/628 Final Project/results/"+datestr+"_Count_by_State.csv"
count_by_category_file = "/Users/juliecarlson/Desktop/628 Final Project/results/"+datestr+"_Count_by_Category.csv"
count_by_area_of_significance_file = "/Users/juliecarlson/Desktop/628 Final Project/results/"+datestr+"_Count_by_Area_of_Significance.csv"
count_by_year_listed_file = "/Users/juliecarlson/Desktop/628 Final Project/results/"+datestr+"_Count_by_Year_Listed.csv"

#write the dictionaries to csv files
with open(count_by_state_file, "w") as newcsvfile:
    header = ['State', 'Count']
    writer = csv.writer(newcsvfile)
    writer.writerow(header)
    for key, value in count_by_state.items():
        writer.writerow([key, value])

with open(count_by_category_file, "w") as newcsvfile:
    header = ['Category of Property', 'Count']
    writer = csv.writer(newcsvfile)
    writer.writerow(header)
    for key, value in count_by_category.items():
        writer.writerow([key, value])

with open(count_by_area_of_significance_file, "w") as newcsvfile:
    header = ['Area of Significance', 'Count']
    writer = csv.writer(newcsvfile)
    writer.writerow(header)
    for key, value in count_by_area_of_significance.items():
        writer.writerow([key, value])

with open(count_by_year_listed_file, "w") as newcsvfile:
    header = ['Year Listed', 'Count']
    writer = csv.writer(newcsvfile)
    writer.writerow(header)
    for key, value in count_by_year_listed.items():
        writer.writerow([key, value])


