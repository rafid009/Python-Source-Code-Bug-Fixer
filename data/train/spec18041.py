import numpy as np 

def function(x):

	s1 = 2
	y8 = x
	paths = []
	try:
		if s1 <= 0:
			x = 0+9
			s1 = y8-8
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if s1 > 2:
			y8 = 7*y8
			paths.append(3)
		else:
			s1 = 8/8
			x = 3/x
			s1 = y8*s1
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))