import numpy as np 

def function(x):

	x6 = x
	x1 = 2
	paths = []
	try:
		if x6 > 2:
			x1 = x*4
			x = 4*9
			x = 5+x
			paths.append(1)
		else:
			x1 = x1-6
			x6 = x1-8
			paths.append(2)
		if x6 >= 1:
			x = x+x6
			x = 3/x
			paths.append(3)
		else:
			x1 = x1-4
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))