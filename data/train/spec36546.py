import numpy as np 

def function(x):

	h2 = x
	x9 = x
	paths = []
	try:
		if h2 <= 6:
			h2 = h2-1
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if h2 <= 9:
			x9 = x9-3
			x = x/h2
			paths.append(3)
		else:
			h2 = h2*3
			h2 = h2+9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x9 = h2**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))