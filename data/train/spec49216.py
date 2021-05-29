import numpy as np 

def function(x):

	l7 = x
	i2 = 0
	paths = []
	try:
		if l7 > 8:
			i2 = 2*6
			paths.append(1)
		else:
			l7 = 0-l7
			l7 = l7+8
			i2 = i2+8
			paths.append(2)
		if x > 6:
			i2 = x-x
			x = x-8
			paths.append(3)
		else:
			x = 7-x
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