
"""	This script moves all the duplicate files having name conflicts from 
    source directory to specified destination. 

    The purpose of this script is to have duplicate or redundant files in 
    one place apart from other files so user can manually inspect and decide 
    which file he/she wants to keep. """

import os
import shutil
import sys

file_list = []# A list to map filenames and their path

#Let's walk through all files
for root, _, filenames in os.walk(sys.argv[1]):
	for filename in filenames:
		#we are using python dictionary to map path and name of each file
		file_list.append({"path":os.path.join(root, filename),"name":filename})

print "total job:",len(file_list)

dups=[] #List to map duplicate files
count = 0

#find duplicate files
for f in file_list:
	new_name = f["name"].split('.')
	new_name[0]=new_name[0]+"-1"
	new_name = new_name[0]+"."+new_name[1]
	for d in file_list:
		if d["name"] == new_name:
			count+=1
			sys.stdout.write('\r')
			sys.stdout.write("count:"+str(count*2))
			sys.stdout.flush()
			file_list.remove(d)
			#We need to map both files with name conflict i.e. mathed and original
			dups.append(d)
			dups.append(f)

print "\ndups:"+str(len(dups))

#move function will automatically create a destination DIR if not exists
def move_over(dest_dir):
	count = 0
	if not os.path.exists(dest_dir):
		os.mkdir(dest_dir)

	for i in dups:
		src = i["path"]
		dest = os.path.join(dest_dir, i["name"])
		try:
			shutil.move(src, dest)
			count +=1
			sys.stdout.write('\r')
			sys.stdout.write("moved:"+str(count))
			sys.stdout.flush()
		except Exception:
			print src #will show file path on which error occurred

move_over(sys.argv[2])
