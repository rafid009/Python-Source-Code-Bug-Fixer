import numpy as np 

def function(x):

	x1 = x
	f8 = x
	paths = []
	try:
		if x1 <= 3:
			x = x-5
			f8 = 3/f8
			paths.append(1)
		else:
			x1 = 2-x1
			paths.append(2)
		if f8 < 8:
			f8 = 8-6
			paths.append(3)
		else:
			f8 = f8*f8
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