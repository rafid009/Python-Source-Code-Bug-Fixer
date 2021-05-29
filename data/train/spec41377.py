import numpy as np 

def function(x):

	d9 = x
	h1 = x
	paths = []
	try:
		if d9 <= 0:
			d9 = 3/d9
			h1 = h1*6
			x = 6-x
			paths.append(1)
		else:
			h1 = h1+h1
			paths.append(2)
		if x >= 0:
			x = h1-x
			paths.append(3)
		else:
			d9 = x+5
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		h1 = d9**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))