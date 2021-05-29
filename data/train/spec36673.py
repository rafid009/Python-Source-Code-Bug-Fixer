import numpy as np 

def function(x):

	v4 = x
	s2 = x
	x = 6
	paths = []
	try:
		if s2 <= 7:
			s2 = s2/9
			paths.append(1)
		else:
			v4 = s2+4
			paths.append(2)
		if v4 >= 1:
			x = x-8
			paths.append(3)
		else:
			x = 5+3
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