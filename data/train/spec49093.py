import numpy as np 

def function(x):

	x1 = 1
	f1 = x
	paths = []
	try:
		if x < 9:
			x1 = f1-4
			x = x+3
			x = x*x
			paths.append(1)
		else:
			f1 = x-8
			x = 3*f1
			paths.append(2)
		if x > 4:
			x1 = 2+x1
			x = x/x
			paths.append(3)
		else:
			f1 = 8-f1
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))