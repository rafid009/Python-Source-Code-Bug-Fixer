import numpy as np 

def function(x):

	l2 = 7
	f8 = 6
	paths = []
	try:
		if x < 9:
			x = x+f8
			x = 4*x
			x = l2*9
			paths.append(1)
		else:
			x = 0-8
			f8 = f8-l2
			x = 6+x
			paths.append(2)
		if l2 < 4:
			l2 = l2-1
			f8 = 9*f8
			f8 = x+l2
			paths.append(3)
		else:
			f8 = 3*x
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