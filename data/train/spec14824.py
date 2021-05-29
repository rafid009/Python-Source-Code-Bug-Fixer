import numpy as np 

def function(x):

	d4 = x
	x4 = x
	paths = []
	try:
		if x > 5:
			x = 0+d4
			x4 = x4-3
			d4 = x/6
			paths.append(1)
		else:
			x = x4/d4
			x4 = x4+8
			paths.append(2)
		if x > 3:
			d4 = d4*d4
			d4 = d4+x
			x4 = x4-5
			paths.append(3)
		else:
			x = x/7
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))