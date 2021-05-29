import numpy as np 

def function(x):

	h9 = x
	g3 = x
	paths = []
	try:
		if g3 > 3:
			g3 = x*x
			g3 = 7/g3
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if h9 < 5:
			x = g3-8
			x = 6/h9
			h9 = 8+1
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))