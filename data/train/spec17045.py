import numpy as np 

def function(x):

	x1 = 5
	l5 = 2
	paths = []
	try:
		if x1 > 6:
			x1 = 5-x
			x = 4*x
			x = 7*l5
			paths.append(1)
		else:
			l5 = 1*x
			x1 = x/8
			paths.append(2)
		if x <= 1:
			l5 = l5+6
			x1 = x1+2
			x1 = x1+7
			paths.append(3)
		else:
			l5 = 2*5
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))