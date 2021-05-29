import numpy as np 

def function(x):

	d4 = 3
	s0 = x
	paths = []
	try:
		if d4 >= 6:
			d4 = d4-x
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if d4 >= 0:
			d4 = 6+d4
			s0 = 8-s0
			x = 6+x
			paths.append(3)
		else:
			s0 = s0/1
			s0 = s0/9
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