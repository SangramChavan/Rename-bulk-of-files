import os
def rename_files():

    saved_path = os.getcwd()
    print ("Current Working Directory is "+saved_path)
    os.chdir(r"/home/unknown/Downloads/prank/prank")

    # get the file names from folder    
    file_list = os.listdir(r"/home/unknown/Downloads/prank/prank")
    print (file_list)
    
    #rename file
    for file_name in file_list:
        print("Old name -"+file_name)
	print("New name -"+file_name.translate(None,"0123456789"))
	os.rename(file_name, file_name.translate(None,"0123456789"))
        
rename_files()
