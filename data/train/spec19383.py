import numpy as np 

def function(x):

	v3 = 7
	h6 = 7
	paths = []
	try:
		if v3 <= 0:
			v3 = v3*1
			h6 = v3*x
			h6 = h6-6
			paths.append(1)
		else:
			h6 = h6/2
			x = x/h6
			paths.append(2)
		if v3 >= 0:
			v3 = v3+7
			v3 = v3+4
			v3 = h6+5
			paths.append(3)
		else:
			h6 = h6/v3
			x = x-h6
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