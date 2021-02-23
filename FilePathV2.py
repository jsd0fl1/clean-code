import re

# Get the directory path of a file path
#  filepath -> the whole path to the file
#  return   -> the directory name without the filename
def get_file(filepath):
    if len(filepath) > 0 and filepath.endswith('/'):
        return filepath

    try:
        location = int(filepath.rindex('/'))
    except:
        location = -1

    if location >= 0:
        dir_name = filepath[0: location + 1]
    else:
        dir_name = '' #sFilename

    return dir_name


# Get the filename of a file path
#  filepath -> the whole path to the file
#  return   -> the filename without the path to the directory
def get_filename_part(filepath):
    try:
        int(filepath.rindex('/'))
    except:
        return filepath

    pos = filepath.rindex('/')
    base_name = filepath[pos + 1:]
    return base_name


# Get the file extension of a file (e.g 'image.png' -> 'png')
#  filepath -> the whole path to the file
#  return   -> the extension of the file
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
