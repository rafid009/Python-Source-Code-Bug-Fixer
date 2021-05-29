import numpy as np 

def function(x):

	d4 = 5
	h2 = x
	paths = []
	try:
		if x <= 2:
			d4 = 6/2
			paths.append(1)
		else:
			x = x+9
			h2 = 5-h2
			d4 = 9-d4
			paths.append(2)
		if x > 0:
			h2 = h2+0
			paths.append(3)
		else:
			d4 = 9*d4
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))