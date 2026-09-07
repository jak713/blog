import os
import shutil

def make_public_dir():
    source = "static/"
    destination = "docs/"

    if not os.path.exists(source):
        print("static path does not exist")
        return
    
    if not os.path.exists(destination):
        os.mkdir(destination)
    else:
        print("removing docs/")
        shutil.rmtree(destination)
        print("creating docs/")
        os.mkdir(destination)

    copy_files(source, destination)
    print("Done!\n\n")


def copy_files(source:str, destination:str):
    # list files in source
    files = os.listdir(source)
    for file in files:
        path = os.path.join(source, file)
        if os.path.isfile(path):
            print(f"Copying file: {file} from {path} to {destination}")
            shutil.copy(src=path, dst=destination)
        else:
            # if file is directory save it as so and recursively run function
            print(f"Invoking copy_file for {path}")
            dir_des = os.path.join(destination, file)
            os.mkdir(dir_des)
            copy_files(source=path, destination=dir_des)

