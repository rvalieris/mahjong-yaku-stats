import numpy
import js2py
import gzip
import sys
import re

m = re.search(r'profs/(\d+)-(\d+).js.gz', sys.argv[1])
year = m.group(1)
month = m.group(2)

a0 = 'total=[];prof=[];updated=[];function load(){};\n'
a1 = open("yaku.js").read()
a2 = gzip.open(sys.argv[1]).read().decode()

prof = js2py.eval_js(a0+a1+a2+'prof')
total = js2py.eval_js(a0+a1+a2+'total')

rooms = {
	0: '一般',
	128: '上級',
	32: '特上',
	160: '鳳凰'
}

modes = {
	1:'東喰赤', 3:'東喰', 7:'東',
	9:'南喰赤', 11:'南喰', 15:'南',
	17:'三東喰赤', 25: '三南喰赤'
}

headers = ['year', 'month', 'room', 'mode', 'total', 'count', 'yaku', 'rate', 'han', 'chan', 'hanp', 'chanp']
print("\t".join(headers))
for i in rooms.keys():
	for j in modes.keys():
		code = i | j
		data = prof[code]
		if data is None:
			continue
		percs = numpy.array(list(map(lambda d: float(d[1]), data)))/100
		counts = numpy.rint(percs*total[code]).astype(int)

		for idx, row in enumerate(data):
			r = [year, month, rooms[i], modes[j], str(total[code]), str(counts[idx])]+row
			print("\t".join(r))

