import numpy as np 

def function(x):

	l5 = x
	s5 = 9
	paths = []
	try:
		if x < 6:
			l5 = l5*x
			x = x-l5
			s5 = 6*s5
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if l5 > 8:
			l5 = 0-1
			paths.append(3)
		else:
			s5 = 4+s5
			x = x-9
			l5 = 5+0
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