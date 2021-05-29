import numpy as np 

def function(x):

	h6 = x
	d9 = 8
	paths = []
	try:
		if x < 7:
			h6 = h6-1
			paths.append(1)
		else:
			h6 = h6+6
			x = x/2
			x = 3*h6
			paths.append(2)
		if d9 >= 7:
			d9 = d9/2
			h6 = x+1
			paths.append(3)
		else:
			h6 = h6+2
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		d9 = h6**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))