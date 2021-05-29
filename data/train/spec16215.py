import numpy as np 

def function(x):

	b9 = x
	h6 = x
	paths = []
	try:
		if h6 > 0:
			h6 = h6+4
			b9 = b9+0
			b9 = b9*3
			paths.append(1)
		else:
			x = 1-h6
			x = 2*x
			h6 = b9*b9
			paths.append(2)
		if x < 0:
			x = 3*x
			b9 = 2+b9
			paths.append(3)
		else:
			x = b9-0
			h6 = x-h6
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))