import errno
import datetime
import os
import shutil
import subprocess
import sys


ROOT_DIR = os.path.dirname(__file__)


def main(argv):
    [_, post] = argv
    today = datetime.date.today()
    destination_folder = os.path.join(
        ROOT_DIR,
        "content",
        "blog",
        str(today.year),
        today.strftime("%b").lower(),
        str(today.day),
    )
    try:
        os.makedirs(destination_folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    destination_file = os.path.join(destination_folder, os.path.basename(post))
    shutil.move(post, destination_file)
    subprocess.check_call(["git", "rm", post])
    subprocess.check_call(["git", "add", destination_file])
    subprocess.check_call(["git", "commit", "-am", "Publish post"])


if __name__ == "__main__":
    main(sys.argv)
