import numpy as np 

def function(x):

	k2 = 0
	s0 = 8
	paths = []
	try:
		if k2 < 9:
			k2 = k2/x
			paths.append(1)
		else:
			k2 = 3+k2
			k2 = x/k2
			paths.append(2)
		if k2 > 4:
			s0 = s0+3
			paths.append(3)
		else:
			x = x*2
			k2 = x*k2
			s0 = 0+k2
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