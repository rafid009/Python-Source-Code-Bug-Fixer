import numpy as np 

def function(x):

	h8 = x
	g0 = x
	paths = []
	try:
		if x > 5:
			h8 = g0+x
			x = x-5
			x = h8/2
			paths.append(1)
		else:
			h8 = 2/h8
			g0 = g0+2
			x = 5/x
			paths.append(2)
		if g0 > 2:
			g0 = g0*5
			g0 = g0+7
			paths.append(3)
		else:
			h8 = h8/6
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))