import numpy as np 

def function(x):

	v1 = x
	h4 = x
	x = 6
	paths = []
	try:
		if h4 <= 9:
			x = 7*x
			paths.append(1)
		else:
			v1 = 4/5
			v1 = 0*v1
			paths.append(2)
		if x > 5:
			v1 = v1*3
			x = v1*5
			paths.append(3)
		else:
			h4 = h4/9
			h4 = h4/3
			x = 8/x
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