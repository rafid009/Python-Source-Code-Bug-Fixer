import numpy as np 

def function(x):

	b3 = 1
	s0 = 7
	paths = []
	try:
		if x > 0:
			x = x/9
			b3 = 7/s0
			paths.append(1)
		else:
			b3 = b3-8
			b3 = b3+7
			paths.append(2)
		if x >= 7:
			s0 = s0+b3
			paths.append(3)
		else:
			b3 = x+b3
			b3 = 4-0
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