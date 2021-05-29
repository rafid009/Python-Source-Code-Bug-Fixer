import numpy as np 

def function(x):

	p4 = 4
	w9 = x
	paths = []
	try:
		if p4 > 5:
			x = x+6
			p4 = p4-6
			p4 = 8*8
			paths.append(1)
		else:
			w9 = x-w9
			p4 = p4+p4
			paths.append(2)
		if x >= 1:
			p4 = 3/p4
			w9 = w9*2
			p4 = p4/7
			paths.append(3)
		else:
			w9 = 2+w9
			x = w9-4
			w9 = w9/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))