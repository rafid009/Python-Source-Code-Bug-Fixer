import numpy as np 

def function(x):

	h6 = x
	v4 = 4
	x = x
	paths = []
	try:
		if h6 <= 9:
			x = x+2
			h6 = 6-h6
			paths.append(1)
		else:
			x = 7*x
			x = 5+x
			v4 = v4/v4
			paths.append(2)
		if v4 < 6:
			x = x+x
			x = x+7
			paths.append(3)
		else:
			x = x-1
			v4 = 0/2
			x = 5+9
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