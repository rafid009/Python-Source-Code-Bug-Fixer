import numpy as np 

def function(x):

	h4 = x
	b0 = 2
	paths = []
	try:
		if x <= 2:
			b0 = b0*2
			h4 = 0*h4
			x = 2/x
			paths.append(1)
		else:
			h4 = h4/h4
			x = h4/7
			paths.append(2)
		if b0 > 4:
			h4 = b0*2
			paths.append(3)
		else:
			h4 = 3-7
			h4 = 9*3
			b0 = 7-9
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