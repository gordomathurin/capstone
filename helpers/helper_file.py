def folder_path(instance, filename):
    return "anime_user_{0}/{1}".format(instance.anime_user.id, filename)
