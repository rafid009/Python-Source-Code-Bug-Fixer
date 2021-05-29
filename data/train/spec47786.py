import numpy as np 

def function(x):

	h2 = x
	d1 = 9
	paths = []
	try:
		if d1 >= 3:
			x = x/5
			h2 = h2/6
			paths.append(1)
		else:
			x = d1+d1
			d1 = 9+8
			d1 = 9*h2
			paths.append(2)
		if d1 <= 6:
			d1 = 4-d1
			d1 = d1/3
			x = d1-x
			paths.append(3)
		else:
			x = d1/x
			d1 = x-9
			x = x/x
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