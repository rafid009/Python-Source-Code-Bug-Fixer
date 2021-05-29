import numpy as np 

def function(x):

	s0 = x
	b5 = 7
	paths = []
	try:
		if x < 5:
			x = 0/x
			paths.append(1)
		else:
			b5 = 8/b5
			paths.append(2)
		if x > 1:
			x = 9/b5
			paths.append(3)
		else:
			s0 = s0-7
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		b5 = s0**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))