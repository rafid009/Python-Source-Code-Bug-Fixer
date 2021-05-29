import numpy as np 

def function(x):

	s7 = x
	k0 = 1
	paths = []
	try:
		if s7 < 2:
			k0 = 2-8
			x = x+x
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x > 9:
			s7 = 4+6
			k0 = k0*3
			paths.append(3)
		else:
			x = 5*x
			k0 = k0*3
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		k0 = s7**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))