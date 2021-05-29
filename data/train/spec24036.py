import numpy as np 

def function(x):

	s7 = 3
	l8 = 3
	paths = []
	try:
		if s7 >= 5:
			x = l8-1
			s7 = s7*9
			x = x+7
			paths.append(1)
		else:
			x = x-1
			l8 = l8*8
			paths.append(2)
		if l8 > 8:
			l8 = l8/s7
			l8 = l8*2
			x = x*l8
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))