import os
UPLOAD_FOLDER = 'E://image//'

files = os.listdir(UPLOAD_FOLDER)
print(type(files))
print(files)

for i in files:
    path = os.path.join(UPLOAD_FOLDER + i)
    print(path)