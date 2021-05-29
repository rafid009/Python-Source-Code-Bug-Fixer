import numpy as np 

def function(x):

	h1 = x
	d0 = 7
	paths = []
	try:
		if d0 >= 5:
			d0 = d0+1
			h1 = h1*h1
			x = x/4
			paths.append(1)
		else:
			x = 9+6
			h1 = 3-h1
			paths.append(2)
		if x > 5:
			h1 = d0-8
			h1 = h1-1
			paths.append(3)
		else:
			h1 = 7/h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))