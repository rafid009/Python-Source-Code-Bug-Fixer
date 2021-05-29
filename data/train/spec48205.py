import numpy as np 

def function(x):

	i5 = 2
	s0 = 3
	paths = []
	try:
		if x <= 0:
			i5 = 6+7
			i5 = i5/5
			x = s0/2
			paths.append(1)
		else:
			x = 3-5
			s0 = 9-s0
			x = i5*x
			paths.append(2)
		if i5 < 2:
			s0 = 6+3
			paths.append(3)
		else:
			i5 = s0+7
			s0 = s0/3
			i5 = i5+6
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