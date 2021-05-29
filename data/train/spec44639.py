import numpy as np 

def function(x):

	z1 = 2
	l9 = x
	paths = []
	try:
		if l9 <= 7:
			x = x+4
			x = 1*x
			l9 = l9/l9
			paths.append(1)
		else:
			l9 = l9-8
			l9 = l9+5
			paths.append(2)
		if x < 5:
			l9 = l9/l9
			l9 = 3+l9
			paths.append(3)
		else:
			x = 0*x
			l9 = l9+0
			x = z1-l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))