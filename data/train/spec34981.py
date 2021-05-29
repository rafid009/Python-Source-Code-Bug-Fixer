import numpy as np 

def function(x):

	x5 = 3
	s0 = 9
	paths = []
	try:
		if x5 < 7:
			x = 1/x
			x5 = x*1
			x = x-4
			paths.append(1)
		else:
			x5 = x5*9
			paths.append(2)
		if x > 8:
			s0 = s0-x5
			x = x*0
			x = 0-x
			paths.append(3)
		else:
			x = x-8
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