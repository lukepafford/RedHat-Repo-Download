#!/usr/bin/python3
from openshift_images import user_images, component_images
from typing import List
from pathlib import Path
from subprocess import run, PIPE
from functools import wraps
from util import get_container_exe
import sys


def main():
    all_images: List[str] = user_images + component_images
    cache_path: Path = Path(sys.argv[0]).resolve().parent / ".images.txt"

    @cache_line_entries(cache_path)
    def process_image(image):
        pull_image(image)

    # Process all images
    for image in all_images:
        process_image(image)

    # Remove the cache file
    cache_path.unlink()


def cache_line_entries(cache_path):
    """
	Writes each item to a single line in a file. If the item
	already exists in the file then skip it. If the item doesn't exist,
	then process the item, and add the entry to the cache. If the program
	ends before processing all the items in the list, then it will resume
	where it left off.
	"""

    def decorator(process):
        @wraps(process)
        def inner(item):
            with open(cache_path, "a+") as cache_handle:
                cache_handle.seek(0)
                cache: List[str] = [line.rstrip() for line in cache_handle.readlines()]
                if item not in cache:
                    process(item)
                    cache_handle.write(f"{item}\n")

        return inner

    return decorator


def pull_image(url: str, retries: int = 3):
    res = run([get_container_exe(), "pull", url], stderr=PIPE, universal_newlines=True)

    # Exit on successful pull
    if res.returncode == 0:
        return

    # This is the main error we want to fix, we likely have a typo in one of our urls
    elif res.stderr.lower().strip().endswith("not found"):
        raise Exception(f"Failed to pull url {url}. Check the spelling of the url")

    # Retry the download if it's any other error, the error is likely on the server end
    elif retries > 0:
        pull_image(url, retries - 1)

    else:
        raise Exception(f"Failed to pull url {url}. Error: {res.stderr}")


if __name__ == "__main__":
    main()
