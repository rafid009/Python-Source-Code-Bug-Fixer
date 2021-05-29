import numpy as np 

def function(x):

	p4 = 6
	r9 = x
	paths = []
	try:
		if r9 < 8:
			r9 = r9+r9
			p4 = p4/p4
			r9 = p4+9
			paths.append(1)
		else:
			r9 = r9-3
			r9 = 7-p4
			r9 = r9*8
			paths.append(2)
		if p4 <= 1:
			p4 = x-p4
			paths.append(3)
		else:
			p4 = p4-2
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