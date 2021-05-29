import numpy as np 

def function(x):

	l8 = x
	x2 = 4
	paths = []
	try:
		if l8 <= 7:
			x = l8*x2
			x = 1+x
			x = 1-x
			paths.append(1)
		else:
			l8 = l8+x
			x2 = 2+x2
			x2 = 7/x2
			paths.append(2)
		if x2 > 0:
			x = x/3
			x = x+5
			paths.append(3)
		else:
			x2 = x2/9
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))