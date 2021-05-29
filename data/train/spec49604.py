import numpy as np 

def function(x):

	x4 = x
	s1 = 1
	paths = []
	try:
		if x <= 6:
			s1 = 7*s1
			s1 = x4*8
			paths.append(1)
		else:
			s1 = s1+2
			x = 9*x
			paths.append(2)
		if x4 <= 2:
			x4 = x/9
			paths.append(3)
		else:
			s1 = 6+8
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