import re


# Get the File path E.g. log/cups/
# sFile is the file path
def get_file(filepath):
    if len(filepath) > 0 and filepath.endswith('/'):
        return filepath

    try:
        p_location = int(filepath.rindex('/'))
    except:
        p_location = -1
    dirName = ''
    if p_location >= 0:
        dirName = filepath[0: p_location + 1]
    else:
        dirName = '' #sFilename

    return dirName


# This function gets the file
def get_filename_part(filepath):
    try:
        int(filepath.rindex('/'))
    except:
        return filepath

    pos = filepath.rindex('/')
    base_name = filepath[pos + 1:]
    return base_name


#.png
def get_extension_part(filepath):
    try:
        occurrences = [m.start() for m in re.finditer('\.', filepath)]
        return filepath[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_file("log/cups/access_log") == "log/cups/")
assert(get_file("log/cups/") == "log/cups/")
assert(get_file("cups/access_log") == "cups/")
assert(get_file("access_log") == "")
assert(get_filename_part("log/cups/access_log") == "access_log")
assert(get_filename_part("log/cups/") == "")
assert(get_filename_part("cups/access_log") == "access_log")
assert(get_filename_part("access_log") == "access_log")
assert(get_extension_part("log/cups/access_log") == "")
assert(get_extension_part("base/FileHelper.cpp") == "cpp")
assert(get_extension_part("base/FileHelper.cpp.bak") == "bak")
