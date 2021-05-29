import numpy as np 

def function(x):

	x1 = 8
	f1 = x
	paths = []
	try:
		if f1 > 8:
			x = 3/x1
			x1 = 6-8
			paths.append(1)
		else:
			x1 = x1/9
			paths.append(2)
		if x < 7:
			x = x*2
			f1 = x1-3
			paths.append(3)
		else:
			f1 = 6-4
			x = f1-4
			x = x1-x
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