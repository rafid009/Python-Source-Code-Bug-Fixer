import numpy as np 

def function(x):

	s0 = x
	e1 = x
	paths = []
	try:
		if e1 >= 0:
			s0 = 4*s0
			s0 = 3-s0
			x = x/2
			paths.append(1)
		else:
			s0 = s0-0
			s0 = e1+s0
			paths.append(2)
		if x <= 0:
			e1 = e1/7
			paths.append(3)
		else:
			s0 = s0/s0
			x = s0+9
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