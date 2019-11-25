#!/usr/bin/python3
from openshift_images import OpenshiftImages
from typing import List
from pathlib import Path
from subprocess import run, PIPE
from functools import wraps
from util import get_container_exe
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import sys, datetime, os


def main():
    parser: ArgumentParser = ArgumentParser(
        description="Downloads, and saves Openshift images for offline loading",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("action", choices=["download", "save"])
    parser.add_argument(
        "--save-output-dir",
        default=Path(os.getcwd(), f"openshift_saved_images_{datetime.date.today()}"),
        required=False,
        help="Directory used to save tar archives. One tar archive per image.",
    )
    parser.add_argument(
        "--openshift-versions",
        nargs="*",
        default=["v3.11.135", "v3.11.153"],
        required=False,
        help="""Openshift versions that are used to tag all required images.
            This argument must be provided after the 'download' positional
            parameter """,
    )

    args = parser.parse_args()
    openshift_images = OpenshiftImages(openshift_versions=args.openshift_versions)

    if args.action == "download":
        cache_path: Path = Path(sys.argv[0]).resolve().parent / ".images.txt"

        @cache_line_entries(cache_path)
        def process_image(image):
            pull_image(image)

        # Process all images
        for image in openshift_images.all_images:
            process_image(image)

        # Remove the cache file
        cache_path.unlink()

    elif args.action == "save":
        save_images(args.save_output_dir, openshift_images.all_images)


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


def save_images(tar_dir: str, images: List[str]):
    os.makedirs(tar_dir, exist_ok=True)
    for image in images:
        filename = f"{tar_dir}/{image.replace('/','_').replace(':', '_')}.tar"
        # Do not save the image if the saved file already exists from a
        # previous execution
        if Path(filename).is_file:
            continue

        # save the image
        res = run(
            [get_container_exe(), "save", "-o", filename, image,],
            stderr=PIPE,
            universal_newlines=True,
        )
        if res.returncode != 0:
            raise ChildProcessError(res.stderr)


if __name__ == "__main__":
    main()
