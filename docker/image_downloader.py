#!/usr/bin/python3
from openshift_images import user_images, component_images
from typing import List
from pathlib import Path
from subprocess import run
import sys

all_images: List[str] = user_images + component_images
cache_name: Path = Path(sys.argv[0]).resolve().parent / '.images.txt'

with open(cache_name, 'a+') as cache_handle:
	cache_handle.seek(0)
	cache: List[str] = [ line.rstrip() for line in cache_handle.readlines() ]

	for image in all_images:
		if image not in cache:
			res = run(['/bin/docker', 'pull', image])
			if res.returncode != 0:
				raise Exception(f'Failed to pull image {image}')
			else:
				# Save successful results to the cache
				cache_handle.write(f'{image}\n')

	# Wipe the cache if all processes succeeded
	cache_handle.truncate()
