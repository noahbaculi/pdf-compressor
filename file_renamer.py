import os

# for ii in [2, 4]:


# print(ii)

path = r"D:\Media\_New\Parks and Recreation\Season 07"  # + str(ii)  # path of the directory where the files/folders to be renamed exist

for string_to_be_replaced, replacement_string in [['.1080p.WEB-DL.x265.10bit.AAC.5.1-ImE[UTR]', ''], ['.', ' '], [' mkv', '.mkv']]:
# for string_to_be_replaced, replacement_string in [['.WEB-DL.x264-[MULVAcoded]', '']]:
    # string_to_be_replaced = f'.'  # this string will be replaced by the string in the next line
    # replacement_string = f' '
    # replacement_string = ''

    for filename in os.listdir(path):
        ## replacing substring
        if string_to_be_replaced in filename:
            try:
                new_filename = filename.replace(string_to_be_replaced, replacement_string)
                os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
                print(f'"{filename}" renamed.')
            except PermissionError:
                print(f'*** {filename} access denied and skipped.')

        ## renaming all files, not replacing substring
        # try:
        #     new_filename = f"{filename[:26] + ' - ' + filename[26:].replace(' - ', ' ')}"
        #     os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        #     print(f'"{filename}" renamed.')
        # except PermissionError:
        #     print(f'*** {filename} access denied and skipped.')

