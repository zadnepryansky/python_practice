import shutil

source = "C:\\Users\\user\\Desktop\\photo_2022-11-30_16-44-45.jpg"

destination = "C:\\Users\\user\\Desktop\\My Study\\Dima.jpg"

# try:
#     shutil.copy(source, destination)
#     print('File opened successfully.')
# except shutil.SameFileError:
#     print('lol')
#
try:
    shutil.move(source, destination)
    print('File opened successfully.')
except shutil.SameFileError:
    print('lol')



