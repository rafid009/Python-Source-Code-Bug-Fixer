import numpy as np 

def function(x):

	h2 = x
	paths = []
	try:
		if x > 2:
			h2 = h2*h2
			paths.append(1)
		else:
			h2 = h2+2
			h2 = 1/3
			paths.append(2)
		if h2 >= 7:
			h2 = 1/h2
			h2 = h2-2
			h2 = 6*h2
			paths.append(3)
		else:
			h2 = h2-0
			h2 = h2+0
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))