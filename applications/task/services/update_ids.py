import os

import music_tag

from applications.utils.constant_template import ConstantTemplate
from applications.utils.send import send


def update_music_info(music_id3_info, is_raw_thumbnail=False):
    for each in music_id3_info:
        f = music_tag.load_file(each["file_full_path"])
        base_filename = ".".join(each["filename"].split(".")[:-1])
        var_dict = {
            "title": f["title"].value,
            "artist": f["artist"].value,
            "album": f["album"].value,
            "filename": base_filename
        }
        if each.get("title", None):
            if "${" in each["title"]:
                f["title"] = ConstantTemplate(each["title"]).resolve_data(var_dict)
            else:
                f["title"] = each["title"]
        if each.get("artist", None):
            if "${" in each["artist"]:
                f["artist"] = ConstantTemplate(each["artist"]).resolve_data(var_dict)
            else:
                f["artist"] = each["artist"]
        if each.get("album", None):
            if "${" in each["album"]:
                f["album"] = ConstantTemplate(each["album"]).resolve_data(var_dict)
            else:
                f["album"] = each["album"]
        if each.get("genre", None):
            f["genre"] = each["genre"]
        if each.get("year", None):
            f["year"] = each["year"]
        if each.get("lyrics", None):
            f["lyrics"] = each["lyrics"]
        if each.get("comment", None):
            f["comment"] = each["comment"]
        if each.get("album_img", None):
            img_data = send().GET(each["album_img"])
            if img_data.status_code == 200:
                f['artwork'] = img_data.content
                if is_raw_thumbnail:
                    f['artwork'] = f['artwork'].first.raw_thumbnail([128, 128])
        f.save()

        if each.get("filename", None):
            if "${" in each["filename"]:
                each["filename"] = ConstantTemplate(each["filename"]).resolve_data(var_dict)
            parent_path = os.path.dirname(each["file_full_path"])
            os.rename(each["file_full_path"], f"{parent_path}/{each['filename']}")
