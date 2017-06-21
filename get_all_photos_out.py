
"""	This script moves all the files from source directory and there respective 
	sub-directories to specified destination. 

	The purpose of this script is to bring all the files in one single folder 
	from give destination and all the sub-directories. """

import os
import shutil
import sys

file_list = [] # A list to map filenames and their path


#Let's walk through all the DIRs and files
for root, _, filenames in os.walk(sys.argv[1]):
	for filename in filenames:
		#we are using python dictionary to map path and name of each file
		file_list.append({"path":os.path.join(root, filename),"name":filename})

print "total files found:",len(file_list)

#move function
def move_over(src_dir, dest_dir='all_files'):
	
	fileList = os.listdir(src_dir)
	count = 0
	
	for i in file_list:
		src = i["path"]
		dest = os.path.join(dest_dir, i["name"])
		try:
			
			""" There might be a possiblity that some how there will be more than one file 
			    with same name or maybe even duplicate files which creates name conflicts. """
			
			if os.path.exists(dest):
				
				""" so, we append '-1' at the end of a file if there's any name conflict. """
				
				new_name = i["path"].split('.')
				new_name[0]=new_name[0]+"-1"
				new_name = new_name[0]+"."+new_name[1]
				os.rename(i["path"],new_name) 
				shutil.move(new_name, dest)
				count +=1
				sys.stdout.write('\r')
				sys.stdout.write("moved:"+str(count))
				sys.stdout.flush()
			else:
				shutil.move(src, dest)
				count +=1
				sys.stdout.write('\r')
				sys.stdout.write("moved:"+str(count))
				sys.stdout.flush()
	
		except Exception:
			print src #will show file path on which error occurred

src_dir = sys.argv[1]  
dest_dir = sys.argv[2]

#create dest DIR if not exists
if not os.path.exists(dest_dir):
	os.mkdir(dest_dir)

move_over(src_dir, dest_dir)

