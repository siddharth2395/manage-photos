# Manage-Photos

what was the purpose of Manage-Photos?

    The basic purpose of Manage-Photos was to organize my photos which were organized in folder stucture.
    My objective was to get all the photos in one folder. Well now you think that why would i write a script to ddo that?
    The answer is simple I'm lezy and there were 300+ folders and 40k pics and i wanted to upload all of those photos to Google Photos.
    it seems simple but the problem was that i had multiple backups of those photos there were redundant files everywhere.
    But I wanted to choose which one should be kept to upload. There were possibilities that two diffrent photos can have same name as old
    cameras were reset there numbers after flashing memmories.

So I wanted to do two things

    1. get all photos in one place out from all the folders and sub-folders.
    2. I wanted to remove duplicate photos based on names.

How to use?

  dir structure

      pwd
      |...../your photos root folder
      |...../other folders
      |.....get_all_photos_out.py
      |.....get_all_dups.py
  
  To move all photos in one folder
      
      python get_all_photos_out.py source_folder_name destination_folder_name
      
          e.g.  python get_all_photos_out.py myphotos all_photos
  To filter out duplicate photos and move them into another folder
      
      python get_all_dups.py folder_with_all_photos duplicate_collection_name
          
          e.g python get_all_dups.py all_photos dups
