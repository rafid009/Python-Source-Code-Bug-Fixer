import numpy as np 

def function(x):

	l7 = x
	s7 = 7
	paths = []
	try:
		if l7 <= 0:
			s7 = s7*9
			paths.append(1)
		else:
			x = 8+x
			s7 = 9+s7
			x = x/x
			paths.append(2)
		if x >= 6:
			l7 = l7*l7
			paths.append(3)
		else:
			l7 = l7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))