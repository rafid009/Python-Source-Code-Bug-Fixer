import numpy as np 

def function(x):

	a6 = x
	a2 = 5
	paths = []
	try:
		if a2 >= 3:
			a2 = x+3
			a6 = 1/a6
			a6 = a6*9
			paths.append(1)
		else:
			a6 = a6-1
			paths.append(2)
		if a2 > 0:
			a6 = a6/8
			a6 = a6/1
			paths.append(3)
		else:
			a6 = a6/2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))