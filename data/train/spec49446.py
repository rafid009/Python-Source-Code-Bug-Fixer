import numpy as np 

def function(x):

	r6 = 9
	d3 = 7
	paths = []
	try:
		if d3 > 6:
			r6 = 5/r6
			paths.append(1)
		else:
			r6 = r6-4
			paths.append(2)
		if r6 < 6:
			r6 = 0-5
			paths.append(3)
		else:
			d3 = d3-7
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))