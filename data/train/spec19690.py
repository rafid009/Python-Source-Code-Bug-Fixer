import numpy as np 

def function(x):

	u2 = 3
	h4 = x
	paths = []
	try:
		if u2 < 2:
			x = 1-x
			u2 = h4*u2
			paths.append(1)
		else:
			u2 = u2*9
			u2 = u2*h4
			u2 = u2/1
			paths.append(2)
		if h4 <= 4:
			x = x-2
			h4 = x/4
			paths.append(3)
		else:
			u2 = 2*u2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))