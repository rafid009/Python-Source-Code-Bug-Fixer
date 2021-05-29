import numpy as np 

def function(x):

	e5 = x
	s0 = x
	paths = []
	try:
		if e5 > 9:
			x = x*x
			paths.append(1)
		else:
			s0 = 2-s0
			e5 = e5-8
			paths.append(2)
		if x <= 2:
			e5 = e5*4
			x = e5+s0
			s0 = s0*e5
			paths.append(3)
		else:
			s0 = x+s0
			x = 1*8
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))