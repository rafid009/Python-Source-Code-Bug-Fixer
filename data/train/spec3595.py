import numpy as np 

def function(x):

	u2 = x
	h9 = x
	paths = []
	try:
		if h9 <= 5:
			u2 = u2*2
			x = 9/x
			u2 = 2+7
			paths.append(1)
		else:
			u2 = 4*2
			u2 = h9-u2
			paths.append(2)
		if x <= 4:
			u2 = 5/1
			h9 = 9*h9
			paths.append(3)
		else:
			h9 = h9/1
			x = x/6
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