import numpy as np 

def function(x):

	v5 = x
	s0 = x
	paths = []
	try:
		if s0 < 4:
			v5 = v5-1
			paths.append(1)
		else:
			v5 = v5+7
			paths.append(2)
		if x < 8:
			s0 = 6+x
			s0 = s0+x
			paths.append(3)
		else:
			x = 9*1
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