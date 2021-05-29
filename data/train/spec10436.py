import numpy as np 

def function(x):

	y6 = x
	a0 = 1
	paths = []
	try:
		if x >= 3:
			a0 = a0-6
			paths.append(1)
		else:
			a0 = a0/4
			paths.append(2)
		if a0 >= 5:
			y6 = y6*2
			paths.append(3)
		else:
			y6 = y6/9
			y6 = y6*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))