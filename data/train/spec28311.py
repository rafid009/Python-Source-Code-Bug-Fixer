import numpy as np 

def function(x):

	v1 = x
	s7 = x
	paths = []
	try:
		if x <= 9:
			v1 = 1-v1
			s7 = x/s7
			paths.append(1)
		else:
			v1 = v1+4
			v1 = x*x
			x = 4*v1
			paths.append(2)
		if s7 < 0:
			v1 = 0*2
			paths.append(3)
		else:
			x = v1/x
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))