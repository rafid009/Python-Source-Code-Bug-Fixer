import numpy as np 

def function(x):

	x2 = 2
	s0 = 5
	paths = []
	try:
		if x2 < 7:
			x2 = 0+8
			paths.append(1)
		else:
			x = x2/4
			x2 = x2-0
			paths.append(2)
		if x <= 5:
			x = x/4
			x2 = s0*x
			x = 5*x2
			paths.append(3)
		else:
			x = x*x2
			s0 = 0*s0
			s0 = 4/5
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))