import numpy as np 

def function(x):

	h2 = x
	d1 = 9
	paths = []
	try:
		if h2 > 8:
			d1 = d1/2
			d1 = 5-d1
			paths.append(1)
		else:
			d1 = d1+8
			paths.append(2)
		if x >= 8:
			x = x/2
			paths.append(3)
		else:
			d1 = 4-6
			d1 = 8-1
			d1 = x-9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))