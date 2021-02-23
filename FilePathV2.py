def get_directory_name(filepath: str):
    if '/' not in filepath:
        return ""

    return filepath[0: filepath.rindex('/') + 1]


def get_filename(filepath: str):
    if '/' not in filepath:
        return filepath

    return filepath[filepath.rindex('/') + 1:]


def get_extension(filepath: str):
    if '.' not in filepath:
        return ''

    return filepath[filepath.rindex('.') + 1: ]


assert (get_directory_name("log/cups/access_log") == "log/cups/")
assert (get_directory_name("log/cups/") == "log/cups/")
assert (get_directory_name("cups/access_log") == "cups/")
assert (get_directory_name("access_log") == "")
assert (get_filename("log/cups/access_log") == "access_log")
assert (get_filename("log/cups/") == "")
assert (get_filename("cups/access_log") == "access_log")
assert (get_filename("access_log") == "access_log")
assert (get_extension("log/cups/access_log") == "")
assert (get_extension("base/FileHelper.cpp") == "cpp")
assert (get_extension("base/FileHelper.cpp.bak") == "bak")
