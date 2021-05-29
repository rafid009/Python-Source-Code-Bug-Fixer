import numpy as np 

def function(x):

	h9 = 4
	v5 = 1
	paths = []
	try:
		if x < 1:
			v5 = 1/x
			x = v5*3
			paths.append(1)
		else:
			v5 = 9-7
			paths.append(2)
		if v5 >= 5:
			v5 = h9*1
			v5 = h9+7
			x = x/3
			paths.append(3)
		else:
			v5 = x-6
			h9 = 7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))