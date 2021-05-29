import numpy as np 

def function(x):

	s0 = 4
	r0 = x
	paths = []
	try:
		if x >= 2:
			x = 3/4
			s0 = s0+r0
			paths.append(1)
		else:
			x = 5*1
			paths.append(2)
		if x <= 5:
			r0 = 0+s0
			x = 8*9
			x = 5-x
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))