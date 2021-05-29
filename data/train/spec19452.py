import numpy as np 

def function(x):

	l7 = 3
	s9 = 9
	paths = []
	try:
		if s9 <= 7:
			l7 = 8+s9
			paths.append(1)
		else:
			s9 = 5-s9
			s9 = l7*s9
			x = 2/x
			paths.append(2)
		if x >= 9:
			x = 2-x
			x = 0/9
			paths.append(3)
		else:
			s9 = s9-1
			s9 = 0/s9
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