import numpy as np 

def function(x):

	e4 = x
	h2 = x
	paths = []
	try:
		if h2 < 4:
			x = 3*4
			paths.append(1)
		else:
			e4 = e4/5
			h2 = 4/h2
			paths.append(2)
		if x < 2:
			e4 = e4/e4
			h2 = 7+e4
			h2 = 8+h2
			paths.append(3)
		else:
			e4 = 9*1
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