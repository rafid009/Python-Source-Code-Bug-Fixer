import numpy as np 

def function(x):

	s1 = 3
	y3 = x
	paths = []
	try:
		if s1 >= 9:
			s1 = s1*5
			paths.append(1)
		else:
			x = x-x
			x = y3/y3
			s1 = s1-6
			paths.append(2)
		if s1 > 2:
			x = y3*y3
			x = x-7
			x = x*2
			paths.append(3)
		else:
			s1 = 3-s1
			s1 = y3/y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))