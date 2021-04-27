import os
path = r'D:\Media\TV Shows\Welcome Back, Kotter\Season 03'  # path of the directory where the files/folders to be renamed exist

string_to_be_replaced = 'Welcome Back, Kotter S03e'  # this string will be replaced by the string in the next line
replacement_string = 'Welcome Back, Kotter - S03E'
# replacement_string = ''

for file in os.listdir(path):
    if string_to_be_replaced in file:
        try:
            os.rename(os.path.join(path, file), os.path.join(path, file.replace(string_to_be_replaced, replacement_string)))
            print(f'"{file}" renamed.')
        except PermissionError:
            print(f'*** {file} access denied and skipped.')
