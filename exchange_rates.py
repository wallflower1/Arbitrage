import urllib2
import sys

def get_exchange(curr_from, curr_to, api_key):
	
	url = 'https://www.exchangerate-api.com/{a}/{b}?k={key}'.format(a=curr_from, b=curr_to, key=api_key)

	try:
		api_req = urllib2.urlopen(url)
		rate = api_req.readline().strip()
		return rate

	except Exception, e:
		return None

def get_rate():
	print "enter API key: "
	api_key = sys.stdin.readline().strip()
	currencies = []
	with open("currency_codes.txt",'r') as curr:
		for line in curr:
			codes = line.split('\t')
			currencies.append(codes[2].strip('\n'))


	with open("graph_edges.txt", 'w') as edges:
		for curr_from in currencies:
			for curr_to in currencies:
				if curr_to == curr_from:
					continue

				exch = get_exchange(curr_from, curr_to, api_key)
			
				if exch != None:
					exch = float(exch)
					edges.write('%s %s %.6f\n' %(currencies.index(curr_from), currencies.index(curr_to),exch))
					print ("%s, %s, %.6f" %(curr_from,curr_to, exch))
				else:
					continue
	return currencies
