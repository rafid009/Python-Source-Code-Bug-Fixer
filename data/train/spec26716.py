import numpy as np 

def function(x):

	v5 = x
	d4 = 1
	paths = []
	try:
		if d4 < 6:
			v5 = 8-3
			d4 = 8/x
			v5 = x-2
			paths.append(1)
		else:
			x = 7*x
			x = 3*d4
			x = x/2
			paths.append(2)
		if v5 >= 0:
			v5 = v5/3
			paths.append(3)
		else:
			d4 = d4*1
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		v5 = d4**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))