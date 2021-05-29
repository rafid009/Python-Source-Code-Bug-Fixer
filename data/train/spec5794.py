import numpy as np 

def function(x):

	s0 = x
	x2 = 5
	paths = []
	try:
		if x <= 7:
			s0 = x2/s0
			paths.append(1)
		else:
			s0 = 3+8
			s0 = 7+s0
			x = s0/8
			paths.append(2)
		if x > 9:
			x = 5-0
			paths.append(3)
		else:
			x2 = x2-3
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x2 = s0**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))