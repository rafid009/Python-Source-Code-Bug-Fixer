import numpy as np 

def function(x):

	s8 = 2
	l3 = x
	paths = []
	try:
		if x < 9:
			x = s8-x
			paths.append(1)
		else:
			x = x/5
			x = 6+x
			paths.append(2)
		if x >= 3:
			s8 = 2-5
			s8 = 9+s8
			s8 = 4-s8
			paths.append(3)
		else:
			s8 = 1-s8
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))