import numpy as np 

def function(x):

	h6 = x
	d0 = 1
	paths = []
	try:
		if x > 5:
			d0 = 7*d0
			x = 6-9
			h6 = d0-7
			paths.append(1)
		else:
			x = d0*2
			paths.append(2)
		if h6 > 5:
			d0 = d0*d0
			paths.append(3)
		else:
			x = x-3
			x = x+h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))