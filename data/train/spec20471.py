import numpy as np 

def function(x):

	x1 = x
	f5 = 4
	paths = []
	try:
		if f5 > 6:
			f5 = 9*1
			f5 = f5+5
			x1 = x1*x
			paths.append(1)
		else:
			f5 = 1*f5
			paths.append(2)
		if x > 4:
			f5 = f5*f5
			x = f5+4
			x1 = 9-x1
			paths.append(3)
		else:
			f5 = 8*1
			x1 = 1/2
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