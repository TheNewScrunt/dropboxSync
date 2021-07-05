#! python3
# dropboxSync.py - Sorts Dropbox "Camera Uploads" directory

import os
import os.path
import shutil

# Source Directory *Update to ask
src_dir = "D:\\Dropbox\\Camera Uploads\\"
# Previous examples as examples.
#src_dir = "C:\\Users\\Jamie\\Dropbox\\Camera Uploads\\"
#src_dir = "C:\\Users\\Jamie\\Dropbox\\python\\projects\\working\\pictures source\\"

# Destination Directory *Update to ask
dest_dir = "Z:\\Dropbox\\Time Travel\\Cloud\\S21U\\"
# Previous examples as examples.
#dest_dir = "Z:\\Time Travel\\Cloud\\Note8\\"
#dest_dir = "C:\\Users\\Jamie\\Dropbox\\python\\projects\\working\\pictures destination\\"

# Files to ignore
ignorefiles = (".dropbox", "desktop")

# Find every file in a given directory
images = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
#print (images)

# Take the first part of each filename and use that as the directory name
for image in images:
    if image.startswith(ignorefiles):
        continue
    filedate = image[:7]
    

    # If the directory doesn't exist, create it
    newdest_dir = os.path.join(dest_dir, filedate)
    if not os.path.exists(newdest_dir):
        os.makedirs(newdest_dir)
    print (newdest_dir)
    if os.path.exists(os.path.join(newdest_dir + "\\" + image)):
        print ('Skipping file already exists: ', image)
        continue
    
    print ('Moving: ', os.path.join(filedate + "\\" + image))
    # Move the file into that directory
    shutil.move(os.path.join(src_dir + image), newdest_dir)

print('All files copied')