import numpy as np 

def function(x):

	y7 = 5
	h2 = 6
	paths = []
	try:
		if x > 6:
			x = y7-x
			paths.append(1)
		else:
			h2 = 9*7
			paths.append(2)
		if h2 >= 4:
			x = h2+x
			h2 = 3-h2
			paths.append(3)
		else:
			x = x+y7
			h2 = x*4
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