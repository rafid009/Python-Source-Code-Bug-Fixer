import numpy as np 

def function(x):

	y9 = 9
	l1 = x
	paths = []
	try:
		if l1 >= 3:
			l1 = 2+y9
			paths.append(1)
		else:
			l1 = l1+l1
			paths.append(2)
		if y9 <= 3:
			x = 9*x
			y9 = y9-8
			x = l1/3
			paths.append(3)
		else:
			x = 2/x
			y9 = y9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))