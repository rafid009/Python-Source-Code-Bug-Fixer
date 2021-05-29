import numpy as np 

def function(x):

	k2 = 6
	a7 = 4
	x = x
	paths = []
	try:
		if a7 >= 5:
			k2 = 1-7
			paths.append(1)
		else:
			a7 = a7-9
			paths.append(2)
		if x < 1:
			x = x/2
			paths.append(3)
		else:
			x = 4-8
			k2 = k2+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))