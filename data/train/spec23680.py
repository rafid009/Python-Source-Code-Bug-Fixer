import numpy as np 

def function(x):

	b5 = x
	s0 = 3
	paths = []
	try:
		if x >= 1:
			s0 = s0-8
			s0 = 2/s0
			paths.append(1)
		else:
			b5 = x/8
			paths.append(2)
		if b5 <= 8:
			s0 = 9/6
			b5 = b5/b5
			paths.append(3)
		else:
			s0 = 3-5
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