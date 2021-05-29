import numpy as np 

def function(x):

	v0 = x
	d4 = x
	paths = []
	try:
		if d4 > 8:
			x = x/7
			x = x-9
			d4 = d4+3
			paths.append(1)
		else:
			d4 = 6*d4
			x = 6*6
			paths.append(2)
		if x > 4:
			d4 = v0-0
			paths.append(3)
		else:
			v0 = v0+d4
			v0 = 3/v0
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		v0 = d4**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))