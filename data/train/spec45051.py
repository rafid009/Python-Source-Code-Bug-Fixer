import numpy as np 

def function(x):

	k2 = x
	s0 = 9
	paths = []
	try:
		if k2 > 6:
			k2 = 0-k2
			s0 = k2*s0
			paths.append(1)
		else:
			x = 6-s0
			s0 = 1*3
			k2 = 7+k2
			paths.append(2)
		if k2 > 6:
			k2 = k2-8
			paths.append(3)
		else:
			k2 = 4+s0
			k2 = 3*k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))