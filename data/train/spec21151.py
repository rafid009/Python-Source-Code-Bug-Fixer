import numpy as np 

def function(x):

	k2 = 3
	s4 = x
	paths = []
	try:
		if x >= 2:
			x = x/9
			paths.append(1)
		else:
			k2 = 4*s4
			x = k2*s4
			paths.append(2)
		if x >= 2:
			k2 = 7/x
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))