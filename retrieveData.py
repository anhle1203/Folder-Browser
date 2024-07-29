import pandas as pd
import os
import csv

def extract_keywords_and_put_in_CSV(root):
    extracted_info = {}

    '''
    For each subfolder in the root_path: 
        find metadata.txt
        extract first line
        split by "," --> turn to a list
        put keywords into a list
        append them to the dictionary
    '''

    for subdir in os.listdir(root):

        subdir_path = os.path.join(root, subdir)

        if os.path.isdir(subdir_path):
            metadata_file = os.path.join(subdir_path, "metadata.txt")

            if os.path.isfile(metadata_file):
                
                with open(metadata_file, "r") as f:
                    first_line = f.readline().strip().lower()
                    
                    #information extract from Keyword: A, B, C --> list [A, B, C]
                    first_line = first_line[9:]
                    # print(first_line)
                    extracted_info[subdir] = first_line

    with open("keywordsList.csv", "w") as k:
        w = csv.writer(k)
        w.writerow(["Folder Name", "Keyword"]) #Add column name first 
        w.writerows(extracted_info.items())





#write root path here
root_path = r"\\racns\department_2$\BusinessIntelligence\Decision Analytics\02_Analytics_Presentation\03_RTO_Analysis"

result = extract_keywords_and_put_in_CSV(root_path)
print("RetrieveData is done!")
