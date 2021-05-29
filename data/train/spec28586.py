import numpy as np 

def function(x):

	i4 = 6
	s2 = 2
	paths = []
	try:
		if x <= 9:
			s2 = 4*7
			s2 = 1*i4
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if i4 > 1:
			s2 = i4-8
			x = x+x
			x = i4+x
			paths.append(3)
		else:
			s2 = x-s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))