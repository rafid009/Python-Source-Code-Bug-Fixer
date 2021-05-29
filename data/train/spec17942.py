import numpy as np 

def function(x):

	g7 = 4
	h6 = x
	x = x
	paths = []
	try:
		if g7 >= 2:
			g7 = g7+6
			x = 3/x
			x = x/3
			paths.append(1)
		else:
			x = x+x
			x = 4-x
			h6 = x*1
			paths.append(2)
		if g7 < 0:
			x = x*8
			x = x-7
			paths.append(3)
		else:
			x = 7+3
			x = x*x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))