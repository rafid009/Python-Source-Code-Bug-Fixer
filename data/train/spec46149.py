import numpy as np 

def function(x):

	s7 = x
	l0 = 9
	paths = []
	try:
		if l0 <= 9:
			x = 3-6
			paths.append(1)
		else:
			x = 3-4
			x = 9*0
			paths.append(2)
		if x > 2:
			s7 = 6-s7
			paths.append(3)
		else:
			l0 = s7+l0
			l0 = 8+s7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))