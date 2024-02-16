#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Here, we import necessary libraries:

#os: Provides functions for interacting with the operating system, such as creating directories (os.makedirs()).
#shutil: Offers high-level operations on files and collections of files, including copying (shutil.copy()).
#time: Allows us to work with time-related functions, although it's not extensively used in this script.
#exit from sys: We import this function to exit the script gracefully in case of errors.

import os
import shutil
import time
from sys import exit


# In[2]:


#This line defines the base path where the folder structure will be created. The r prefix denotes a raw string literal in Python, which is used to prevent the backslashes from being treated as escape characters.
base_path = r'C:\Users\Mpho\OneDrive - University of Witwatersrand\Documents'


# In[3]:


#This function takes two parameters: folders (a list of folder names to be created) and base_directory (the base path where folders will be created).
#Inside the function, it iterates through each folder name in the list.
#It constructs the full path of each folder using os.path.join() to ensure compatibility across different operating systems.
#Then, it creates each folder using os.makedirs(), which allows creating directories recursively.
#If any error occurs during folder creation, it prints an error message and exits the script using exit().

def create_folders(folders, base_directory):
    try:
        for folder in folders:
            folder_path = os.path.join(base_directory, folder)
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
    except Exception as e:
        print(f"Error creating folders: {e}")
        exit()


# In[4]:


#This list contains the folder structure to be created. Each element in the list represents a folder path relative to the base directory. The os.path.join() function is used to construct these paths safely.

folders_to_create = [
    'example_project',
    os.path.join('example_project', 'characters'),
    os.path.join('example_project', 'environment_design'),
    os.path.join('example_project', 'script'),
    os.path.join('example_project', 'storyboard'),
    os.path.join('example_project', 'characters', 'Main_character_Mpho')
]


# In[5]:


#This line calls the create_folders() function with the list of folder paths (folders_to_create) and the base path (base_path) as arguments, triggering the creation of the folder structure.
create_folders(folders_to_create, base_path)


# In[ ]:





# In[ ]:




