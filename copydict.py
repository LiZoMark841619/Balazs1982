def CopyDict(old_dict):
    new_dict = {key: old_dict[key] for key in old_dict}
    return new_dict