import numpy as np 

def function(x):

	h1 = x
	l8 = 8
	x = x
	paths = []
	try:
		if x > 5:
			l8 = 6*h1
			x = h1/h1
			paths.append(1)
		else:
			x = x-2
			l8 = l8/5
			x = 9*x
			paths.append(2)
		if x <= 0:
			l8 = l8/l8
			paths.append(3)
		else:
			l8 = 5*l8
			h1 = 3*9
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))