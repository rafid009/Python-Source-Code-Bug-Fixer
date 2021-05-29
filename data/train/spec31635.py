import numpy as np 

def function(x):

	s8 = x
	s9 = x
	paths = []
	try:
		if x <= 2:
			x = x+8
			s8 = 8*s8
			s8 = s8*s9
			paths.append(1)
		else:
			s9 = 9-s9
			paths.append(2)
		if s9 >= 8:
			x = x+3
			paths.append(3)
		else:
			x = x/3
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