import numpy as np 

def function(x):

	s0 = 4
	s5 = 0
	paths = []
	try:
		if s5 >= 1:
			s0 = 0*x
			paths.append(1)
		else:
			s5 = s5+2
			s0 = 5+6
			x = x/9
			paths.append(2)
		if s5 > 9:
			s5 = 8/s5
			x = x/8
			paths.append(3)
		else:
			x = x+4
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