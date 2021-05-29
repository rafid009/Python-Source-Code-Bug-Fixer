import numpy as np 

def function(x):

	f6 = 7
	x6 = 3
	paths = []
	try:
		if x <= 4:
			x = x-6
			paths.append(1)
		else:
			f6 = x*x
			paths.append(2)
		if x6 <= 6:
			f6 = f6-4
			f6 = f6/2
			f6 = 6/f6
			paths.append(3)
		else:
			x6 = x-x6
			x6 = x6*f6
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))