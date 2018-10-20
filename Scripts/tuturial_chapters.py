"""
Utility module for processing the files in the Chapters folder
"""
import os
import shutil
import json
import datetime
import tuturial_navigation


def clean_folder(dest_folder):
    # Check to see if the folder exixt
    if os.path.exists(dest_folder):
        # Remove the folder
        print("Removing old content [%s]" % dest_folder)
        shutil.rmtree(dest_folder)


def copy_content(src_folder, dest_folder):
    # Copy files
    print("Copying content [%s => %s]" % (src_folder, dest_folder))
    shutil.copytree(src_folder, dest_folder)


def build_file_list(dest_folder):
    # The reply which will this function will return
    content = {}

    # Get the list of files in the directory
    for root, folders, files in os.walk(dest_folder):

        # Get the folder names
        for folder in folders:
            # store the full file name
            folder_name = os.path.join(root, folder)
            # Store all the files in this chapter
            content[folder_name] = {
                "files": []
            }

        # Get the path of all files.
        for filename in files:
            # store the full file name
            file_name = os.path.join(root, filename)
            content[os.path.dirname(file_name)]["files"].append(file_name)

    return content


def build_chapters(dest_folder):
    print("Building chapters list")
    # The variable which will store all the structure
    chapters = {}

    # Build list of files
    content = build_file_list(dest_folder)

    # Extract the chapters list and sort them
    folders = list(content)

    # Make sure the list is sorted
    folders.sort()

    # Set the chapters list
    for index in range(len(folders)):
        folder_name = folders[index]
        chapters[folder_name] = {
            "files": content[folders[index]]["files"]
        }

        # Make sure the files are sorted
        chapters[folder_name]["files"].sort()

        if index > 0:
            chapters[folder_name]["prev_chapter"] = folders[index-1]

        # Set next chapter if any
        if index < len(folders)-1:
            chapters[folder_name]["next_chapter"] = folders[index+1]

    # Add teh chapters section to the readme
    tuturial_navigation.add_list_of_content(dest_folder, chapters)

    return chapters


def build_files(dest_folder):
    print("Building files list")

    # Store the content of the files
    files = {}

    # get the content of each chapter
    chapters = build_chapters(dest_folder)

    # Build the files list
    folders = list(chapters)

    # Make sure the list is sorted
    folders.sort()

    # Set the chapters list
    for index in range(len(folders)):
        current_chapter = chapters[folders[index]]

        # Get the path of all files.
        for filename in current_chapter["files"]:
            files[filename] = {
                "file_name": filename
            }
            if current_chapter.get("prev_chapter"):
                files[filename]["prev_chapter"] = current_chapter["prev_chapter"]

            if current_chapter.get("next_chapter"):
                files[filename]["next_chapter"] = current_chapter["next_chapter"]

    return files


def build_content(src_folder, dest_folder):
    print("Building content")

    clean_folder(dest_folder)
    copy_content(src_folder, dest_folder)

    files = build_files(dest_folder)
    files_list = list(files)

    # Make sure teh list is sorted
    files_list.sort()

    for index, filename in enumerate(files_list):

        if index > 0:
            files[filename]["prev_page"] = files_list[index-1]

        # Set next chapter if any
        if index < len(files_list)-1:
            files[filename]["next_page"] = files_list[index+1]

    return files
