import re


def get_directory_name(filepath: str):
    if '/' not in filepath:
        return ""

    return filepath[0: filepath.rindex('/') + 1]


def get_filename(filepath: str):
    if '/' not in filepath:
        return filepath

    return filepath[filepath.rindex('/') + 1:]


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


assert (get_directory_name("log/cups/access_log") == "log/cups/")
assert (get_directory_name("log/cups/") == "log/cups/")
assert (get_directory_name("cups/access_log") == "cups/")
assert (get_directory_name("access_log") == "")
assert (get_filename("log/cups/access_log") == "access_log")
assert (get_filename("log/cups/") == "")
assert (get_filename("cups/access_log") == "access_log")
assert (get_filename("access_log") == "access_log")
assert (get_extension_part("log/cups/access_log") == "")
assert (get_extension_part("base/FileHelper.cpp") == "cpp")
assert (get_extension_part("base/FileHelper.cpp.bak") == "bak")
