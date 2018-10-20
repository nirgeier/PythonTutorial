import datetime
import os
import shutil
import json

current_year = str(datetime.datetime.now().year)


def add_navigation(files):
    print("Adding navigation")

    for filename in list(files):
        current = files[filename]
        navigation = ""
        if current.get("prev_chapter"):
            navigation = "[Previous Chapter](/" + \
                current["prev_chapter"] + ") | "

        if current.get("prev_page"):
            navigation += "[Previous page](/" + current["prev_page"] + ") | "

        navigation += "[List of contents](/README.md#chapters) | "

        if current.get("next_page"):
            navigation += "[Next Page](/" + current["next_page"] + ") | "

        if current.get("next_chapter"):
            navigation += "[Next Chapter](/" + current["next_chapter"] + ")"

        navigation += "\n\n&copy; " + current_year + " CodeWizardAcademy, Inc.\n\n"

        with open(current["file_name"], "a") as myfile:
            myfile.write(navigation.replace("\\", "/"))


def add_list_of_content(dest_folder, chapters):
    print("Adding content list")

    list_of_content = "### Chapters\n\n"
    for chapter in chapters:
        list_of_content += "- [" + \
            os.path.basename(chapter) + "](/" + chapter + ")  \n"

        for file_name in chapters[chapter]["files"]:
            list_of_content += "    - [" + \
                os.path.basename(file_name) + "](/" + file_name + ")  \n"

    list_of_content += "\n\n&copy; " + \
        str(datetime.datetime.now().year) + " CodeWizardAcademy, Inc.\n\n"

    shutil.copy(dest_folder + "/../src/README.md", dest_folder)

    with open(dest_folder + "/README.md", "a") as readme:
        readme.write(list_of_content.replace("\\", "/"))
