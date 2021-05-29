import numpy as np 

def function(x):

	l9 = 2
	s2 = 3
	paths = []
	try:
		if x < 1:
			l9 = l9*6
			paths.append(1)
		else:
			s2 = 8-s2
			s2 = x*4
			l9 = 2+3
			paths.append(2)
		if l9 > 2:
			x = 8/x
			s2 = s2/5
			paths.append(3)
		else:
			s2 = 1/1
			x = x+7
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