#!/usr/bin/python3
from openshift_images import user_images, component_images
from typing import List
from pathlib import Path
from subprocess import run
import sys
import pickle

all_images: List[str] = user_images + component_images
cache_name: Path = Path(sys.argv[0]).resolve().parent / '.images.pickle'

with open(cache_name, 'ab+') as cache_handle:
	cache_handle.seek(0)
	try:
		cache: List[str] = pickle.load(cache_handle)
	except EOFError:
		cache: List[str] = []

	for image in all_images[0:1]:
		res = run(['/bin/docker', 'pull', image])
		if res.returncode != 0:
			# Dump current amount of successful jobs before failing
			pickle.dump(cache, cache_handle)	
			raise Exception(f'Failed to pull image {image}')
		else:
			cache.append(image)	

	# Wipe the cache if all processes succeeded
	pickle.dump([], cache_handle)
