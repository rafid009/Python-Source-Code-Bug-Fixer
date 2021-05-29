import numpy as np 

def function(x):

	s6 = 6
	l3 = x
	x = 3
	paths = []
	try:
		if l3 >= 1:
			l3 = x*s6
			paths.append(1)
		else:
			x = x-9
			x = 7/x
			paths.append(2)
		if x < 5:
			x = x*s6
			paths.append(3)
		else:
			s6 = 4-s6
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