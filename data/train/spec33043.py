import numpy as np 

def function(x):

	n5 = 4
	s0 = x
	paths = []
	try:
		if x < 8:
			x = 6-x
			s0 = 7/7
			x = x+s0
			paths.append(1)
		else:
			n5 = n5-5
			paths.append(2)
		if n5 >= 7:
			s0 = 1+s0
			x = 8*x
			paths.append(3)
		else:
			n5 = n5+1
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