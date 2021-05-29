import numpy as np 

def function(x):

	d7 = x
	r4 = 9
	paths = []
	try:
		if r4 < 6:
			d7 = 4*d7
			r4 = 4/r4
			paths.append(1)
		else:
			x = 7/d7
			d7 = d7/3
			paths.append(2)
		if d7 > 3:
			d7 = 8-d7
			paths.append(3)
		else:
			r4 = r4*6
			r4 = r4*r4
			d7 = d7/x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		r4 = d7**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))