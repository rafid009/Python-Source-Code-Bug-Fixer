import numpy as np 

def function(x):

	d1 = x
	b4 = x
	paths = []
	try:
		if b4 > 0:
			d1 = 3/d1
			paths.append(1)
		else:
			b4 = d1-x
			paths.append(2)
		if x >= 6:
			x = 4/d1
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))