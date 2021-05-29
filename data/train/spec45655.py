import numpy as np 

def function(x):

	h3 = 1
	e4 = x
	paths = []
	try:
		if e4 < 1:
			e4 = e4/5
			x = x+6
			e4 = e4+e4
			paths.append(1)
		else:
			e4 = x*e4
			h3 = e4+1
			h3 = 7-5
			paths.append(2)
		if h3 > 3:
			h3 = 4+h3
			h3 = 2*4
			paths.append(3)
		else:
			e4 = h3+e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))