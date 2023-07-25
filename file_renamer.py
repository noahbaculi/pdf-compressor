import os
import re

path = r"A:\Pentatonix"  # + str(ii)  # path of the directory where the files/folders to be renamed exist


filenames = os.listdir(path)
filenames.sort()
print(path, filenames)
for episode, filename in enumerate(filenames):
    ## replacing substring
    try:
        new_filename = filename
        for string_to_be_replaced, replacement_string in [
            [" - Pentatonix", ""],
            # ["S01OAD", "S00E"],
            # [".", " "],
            # [" mkv", ".mkv"],
        ]:
            if string_to_be_replaced in new_filename:
                new_filename = new_filename.replace(string_to_be_replaced, replacement_string)
        print(f'"{filename}" -> "{new_filename}".')

        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
    except PermissionError:
        print(f"*** {filename} access denied and skipped.")

    ## renaming all files, not replacing substring
    # try:
    #     # index_of_dash = filename.index('-')
    #     if True:
    #         # ep = int(filename[17:20])
    #         # new_ep = ep-277
    #         ext = filename[-4:]
    #         new_filename = f"{filename[:-15]}{ext}"
    #         # new_filename = filename.replace(f'Naruto {episode}', f'Naruto - S{season:02d}E{episode:03d}')
    #         print(f'"{filename}" renamed to "{new_filename}".')
    #
    #         # os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
    # except PermissionError:
    #     print(f'*** {filename} access denied and skipped.')

    print()
