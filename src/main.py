import os
import shutil

from copystatic import copy_file_recursive

dir_path_static = "/home/sirdisalot/static_site_generator/static"
dir_path_public = "/home/sirdisalot/static_site_generator/public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_file_recursive(dir_path_static, dir_path_public)

main()
