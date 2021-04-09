from os import path
from glob import glob

dir = r"C:\Users\Noah Baculi\Documents\Personal Google Drive\Scratch\Downloads"

pdf_files = glob(path.join(dir,"*.{}".format('pdf')))