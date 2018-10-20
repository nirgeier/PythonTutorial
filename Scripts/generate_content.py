import json
import tuturial_chapters
import tuturial_navigation

src_folder = "src/Chapters"
dest_folder = "Chapters"

files = tuturial_chapters.build_content(src_folder, dest_folder)
tuturial_navigation.add_navigation(files)
