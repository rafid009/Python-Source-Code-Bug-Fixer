import numpy as np 

def function(x):

	h7 = 0
	r8 = x
	paths = []
	try:
		if h7 < 3:
			r8 = r8/7
			h7 = h7*h7
			h7 = h7*8
			paths.append(1)
		else:
			r8 = 7*4
			x = x*h7
			h7 = 8*5
			paths.append(2)
		if h7 <= 9:
			x = 3+x
			x = 1/x
			x = x/4
			paths.append(3)
		else:
			x = 3-x
			h7 = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))