import re
filename = 'stamped_file_name_085373.txt'
filename = re.sub(r"_\d{6}$", "", filename)
print filename

