import numpy as np 

def function(x):

	h1 = x
	d0 = 5
	paths = []
	try:
		if x >= 9:
			x = x+6
			x = x-1
			paths.append(1)
		else:
			h1 = h1/8
			d0 = d0+6
			paths.append(2)
		if d0 >= 5:
			d0 = 1*d0
			d0 = 7+d0
			d0 = d0/9
			paths.append(3)
		else:
			d0 = 5-4
			x = d0/d0
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