#Change the values in CAPITALS
# importing required modules 
from zipfile import ZipFile 
import os 
import shutil
  
def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths         
  
def main(): 
    # path to folder which needs to be zipped 
    directory = 'CHANGE ME1'
  
    # calling function to get all file paths in the directory 
    file_paths = get_all_file_paths(directory) 
  
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
  
    # writing files to a zipfile 
    with ZipFile('FULLPATH/NAMEOFFOLDER','w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file)
			
	#Deleting the File that has been Zipped
    shutil.rmtree("CHANGE ME1")
  
    print('All files zipped successfully!')         
  
  
if __name__ == "__main__": 
    main() 