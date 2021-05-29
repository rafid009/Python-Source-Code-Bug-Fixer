import numpy as np 

def function(x):

	l2 = x
	h1 = x
	paths = []
	try:
		if x <= 1:
			l2 = 0+3
			x = x/1
			paths.append(1)
		else:
			x = x+8
			h1 = 7/h1
			x = x+5
			paths.append(2)
		if x > 3:
			l2 = 9+7
			paths.append(3)
		else:
			x = x+3
			h1 = h1/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))