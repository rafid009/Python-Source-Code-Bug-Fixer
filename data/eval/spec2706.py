import numpy as np 

def function(x):

	l5 = 6
	y9 = 5
	paths = []
	try:
		if l5 >= 2:
			l5 = 9*l5
			y9 = l5+y9
			paths.append(1)
		else:
			y9 = 7-y9
			l5 = 7/x
			paths.append(2)
		if x < 2:
			l5 = 8/l5
			paths.append(3)
		else:
			x = 0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))