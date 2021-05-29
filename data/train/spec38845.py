import numpy as np 

def function(x):

	h4 = x
	g3 = 0
	paths = []
	try:
		if x <= 8:
			x = x/2
			h4 = h4*1
			h4 = h4+5
			paths.append(1)
		else:
			g3 = 3+9
			x = 0/x
			g3 = 9-g3
			paths.append(2)
		if x <= 5:
			g3 = 3-6
			h4 = h4/3
			paths.append(3)
		else:
			x = x*h4
			g3 = 9-g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))