import os
import re

path = r"D:\Media\_New\Arcane (2021)\Season 01"  # + str(ii)  # path of the directory where the files/folders to be renamed exist

for string_to_be_replaced, replacement_string in [
    [" (1080p NF WEB-DL x265 t3nzin)", ""],
    # ['S2 - ', '- S02E'],
    # [' S2 - ', ' - S02E']
]:
    # for season in range(1, 10):
    #     path = r'{}'.format(f"D:\Media\_New\Dragon Ball Z\Season {season:02d}")
    #     string_to_be_replaced = 'Dragon Ball Z - '
    #     replacement_string = f'Dragon Ball Z - S{season:02d}E'

    filenames = os.listdir(path)
    filenames.sort()

    print(path, filenames)

    for episode, filename in enumerate(filenames):

        ## replacing substring
        if string_to_be_replaced in filename:
            try:
                new_filename = filename.replace(string_to_be_replaced, replacement_string)
                print(f'"{filename}" renamed to "{new_filename}".')

                os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            except PermissionError:
                print(f'*** {filename} access denied and skipped.')

        ## renaming all files, not replacing substring
        # try:
        #     # index_of_dash = filename.index('-')
        #     new_filename = filename[0:-15] + '.mkv'
        #     # new_filename = filename.replace(f'Naruto {episode}', f'Naruto - S{season:02d}E{episode:03d}')
        #     # new_filename = f'Fairy Tail - {episode+176:03d}'
        #     print(new_filename)
        #
        #     # os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        # except PermissionError:
        #     print(f'*** {filename} access denied and skipped.')

    print()

