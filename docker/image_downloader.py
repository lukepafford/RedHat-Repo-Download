#!/usr/bin/python3
from openshift_images import user_images, component_images
from typing import List
from pathlib import Path
from subprocess import run
import sys
import json
from json.decoder import JSONDecodeError

all_images: List[str] = user_images + component_images
cache_name: Path = Path(sys.argv[0]).resolve().parent / '.images.json'

with open(cache_name, 'a+') as cache_handle:
	cache_handle.seek(0)
	try:
		cache: List[str] = json.load(cache_handle)
	except JSONDecodeError:
		cache: List[str] = []

	for image in all_images:
		if image not in cache:
			res = run(['/bin/docker', 'pull', image])
			if res.returncode != 0:
				# We had an error, Save results so we don't repeat on next run
				# and start back up on the image that caused the error
				json.dump(cache, cache_handle)	
				raise Exception(f'Failed to pull image {image}')
			else:
				cache.append(image)	

	# Wipe the cache if all processes succeeded
	json.dump([], cache_handle)
