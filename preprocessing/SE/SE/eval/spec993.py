import numpy as np 

def function(x):

	h7 = x
	r2 = x
	paths = []
	try:
		if r2 <= 1:
			h7 = 9*h7
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x >= 6:
			h7 = h7*2
			paths.append(3)
		else:
			x = 3*8
			x = x*6
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))