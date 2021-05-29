import numpy as np 

def function(x):

	p2 = x
	r4 = 6
	paths = []
	try:
		if r4 < 0:
			x = x/5
			paths.append(1)
		else:
			x = x/8
			x = r4/8
			x = x-6
			paths.append(2)
		if x >= 2:
			p2 = p2-3
			paths.append(3)
		else:
			p2 = p2+5
			x = x*7
			r4 = r4-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))