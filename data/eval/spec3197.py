import numpy as np 

def function(x):

	n0 = x
	s9 = 2
	paths = []
	try:
		if n0 < 7:
			x = 9+x
			s9 = n0*6
			paths.append(1)
		else:
			s9 = n0/7
			paths.append(2)
		if n0 < 5:
			x = x*3
			paths.append(3)
		else:
			s9 = s9*1
			n0 = s9+n0
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