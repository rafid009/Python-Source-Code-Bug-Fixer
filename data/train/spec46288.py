import numpy as np 

def function(x):

	o3 = x
	s1 = 3
	paths = []
	try:
		if s1 > 8:
			s1 = s1/x
			o3 = o3-2
			paths.append(1)
		else:
			s1 = s1*8
			paths.append(2)
		if s1 > 2:
			o3 = 9*o3
			paths.append(3)
		else:
			s1 = x/o3
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