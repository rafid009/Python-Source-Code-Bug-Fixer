import numpy as np 

def function(x):

	s0 = 2
	o4 = x
	paths = []
	try:
		if x <= 2:
			o4 = o4-5
			s0 = 0/s0
			paths.append(1)
		else:
			s0 = 7*s0
			o4 = o4/x
			o4 = 4-x
			paths.append(2)
		if x <= 4:
			x = o4+x
			paths.append(3)
		else:
			s0 = 5-8
			o4 = 9/o4
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