import numpy as np 

def function(x):

	h3 = 1
	d2 = x
	paths = []
	try:
		if d2 <= 3:
			d2 = d2/x
			paths.append(1)
		else:
			h3 = d2-8
			x = x+8
			d2 = d2-1
			paths.append(2)
		if h3 <= 9:
			h3 = h3/2
			d2 = h3-7
			paths.append(3)
		else:
			d2 = d2*9
			d2 = h3-x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		d2 = h3**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))