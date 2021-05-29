import numpy as np 

def function(x):

	r9 = 5
	h3 = 4
	paths = []
	try:
		if h3 <= 7:
			h3 = 3*h3
			paths.append(1)
		else:
			h3 = r9*h3
			paths.append(2)
		if x <= 7:
			x = 4+h3
			h3 = 5-h3
			paths.append(3)
		else:
			x = x*6
			r9 = 2/x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))