import numpy as np 

def function(x):

	s1 = 3
	e8 = 1
	paths = []
	try:
		if x > 3:
			s1 = 8+s1
			x = 1/x
			s1 = 2-s1
			paths.append(1)
		else:
			e8 = e8/1
			paths.append(2)
		if e8 >= 9:
			s1 = 2/s1
			e8 = e8/s1
			paths.append(3)
		else:
			s1 = 8-s1
			e8 = 3-e8
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