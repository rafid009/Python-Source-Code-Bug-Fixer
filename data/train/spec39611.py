import numpy as np 

def function(x):

	v1 = x
	h6 = x
	paths = []
	try:
		if v1 <= 2:
			h6 = h6+3
			paths.append(1)
		else:
			v1 = v1*x
			x = x*4
			paths.append(2)
		if x >= 5:
			v1 = 1/v1
			h6 = 4+7
			x = 0*x
			paths.append(3)
		else:
			h6 = 5*h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))