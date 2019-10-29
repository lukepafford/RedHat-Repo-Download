from image_downloader import cache_line_entries
from tempfile import mkstemp
from typing import List
import os

def test_line_entries():
	_, temp_file = mkstemp()
	
	try:
		# nums is a list of strings because the cache were testing reads
		# the items as strings
		nums: List[str] = ['1', '2', '3', '4', '5']
		with open(temp_file, 'w') as test_handle:
			for n in range(1, 4):
				test_handle.write(f'{n}\n')
	
		def check_num_greater_than_four(num):
			assert num >= '4'
		
		@cache_line_entries(temp_file)
		def process_nums(num):
			check_num_greater_than_four(num)
	
		for num in nums:
			process_nums(num)
	finally:
		os.remove(temp_file)	
