import os
import datetime

__all__ = ('save_user_stats',)


def get_tsv_line(dictionary):
    s = ""
    for key in sorted(dictionary):
        s += str(dictionary[key]) + "\t"
    return s[:-2] + "\n"


def get_header_line(dictionary):
    s = "\t".join(dictionary)
    return s + "\n"


def dump_data(data, path):
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(get_header_line(data))
            f.write(get_tsv_line(data))
    else:
        with open(path, "a") as f:
            f.write(get_tsv_line(data))


def save_user_stats(self, username):
    user_id = self.convert_to_user_id(username)
    infodict = self.get_user_info(user_id)
    if infodict:
        data_to_save = {}
        data_to_save["date"] = str(datetime.datetime.now())
        data_to_save["followers"] = int(infodict["follower_count"])
        data_to_save["following"] = int(infodict["following_count"])
        data_to_save["medias"] = int(infodict["media_count"])
        dump_data(data_to_save, "%s.tsv" % username)
    self.logger.info("Stats saved at %s." % data_to_save["date"])
    return False
