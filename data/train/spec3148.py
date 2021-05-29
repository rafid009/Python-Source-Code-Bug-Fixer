import numpy as np 

def function(x):

	h6 = 4
	z5 = 7
	paths = []
	try:
		if x > 8:
			z5 = h6+x
			paths.append(1)
		else:
			x = 0*z5
			h6 = h6+7
			paths.append(2)
		if h6 < 7:
			x = z5-7
			h6 = 3/9
			paths.append(3)
		else:
			x = x*1
			h6 = z5-h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		z5 = h6**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))