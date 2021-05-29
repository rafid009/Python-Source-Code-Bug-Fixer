import numpy as np 

def function(x):

	s0 = 5
	u6 = 5
	paths = []
	try:
		if u6 >= 6:
			s0 = u6*3
			x = x-4
			paths.append(1)
		else:
			s0 = s0+7
			u6 = 3+u6
			paths.append(2)
		if x >= 6:
			s0 = s0+1
			paths.append(3)
		else:
			x = 3-x
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