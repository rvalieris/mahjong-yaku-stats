
import requests
import time
import random
import os.path
import sys

headers = {
	'User-Agent': 'Wget/1.21.3',
	'Accept-Encoding': 'identity'
}

for year in range(2007, 2023+1):
	for month in range(1, 12+1):
		month = f'{month:02d}'
		target = f'{year}-{month}'
		target_url = f'https://tenhou.net/sc/{year}/{month}/prof.js'
		print(f'{target_url} . . . ', end='')
		time.sleep(random.uniform(1,5))
		r = requests.get(target_url, headers=headers)
		if r.status_code != 200:
			print(f"error: {target_url}")
			sys.exit(1)

		stuf = r.content
		print(len(stuf))
		path = os.path.join('pages',f'{target}.js')
		open(path, 'wb').write(stuf)

