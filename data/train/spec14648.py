import numpy as np 

def function(x):

	h1 = 1
	g0 = 3
	paths = []
	try:
		if h1 <= 2:
			h1 = h1+1
			x = g0*x
			g0 = 4/g0
			paths.append(1)
		else:
			x = x-x
			h1 = h1/h1
			paths.append(2)
		if h1 <= 3:
			g0 = 2+x
			h1 = h1-h1
			paths.append(3)
		else:
			x = h1/6
			x = x*2
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))