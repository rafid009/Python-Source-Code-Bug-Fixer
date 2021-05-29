import numpy as np 

def function(x):

	y5 = 0
	f1 = x
	paths = []
	try:
		if f1 >= 4:
			x = 7*x
			f1 = 6-2
			paths.append(1)
		else:
			x = x+5
			y5 = 3/6
			paths.append(2)
		if x > 1:
			x = 3/x
			y5 = y5*7
			paths.append(3)
		else:
			f1 = 0-4
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