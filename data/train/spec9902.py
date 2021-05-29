import numpy as np 

def function(x):

	x1 = x
	f1 = 3
	paths = []
	try:
		if x >= 4:
			x1 = 3*9
			x1 = 3-1
			f1 = f1*4
			paths.append(1)
		else:
			f1 = f1*4
			paths.append(2)
		if x < 9:
			x = 7+x
			paths.append(3)
		else:
			x1 = x1/8
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