import numpy as np 

def function(x):

	d4 = x
	h3 = x
	x = x
	paths = []
	try:
		if d4 >= 6:
			x = x-8
			x = x+d4
			paths.append(1)
		else:
			x = x+d4
			h3 = h3-1
			x = x/7
			paths.append(2)
		if x < 4:
			x = x/9
			x = x*1
			paths.append(3)
		else:
			d4 = d4*h3
			d4 = 3*d4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		h3 = d4**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))