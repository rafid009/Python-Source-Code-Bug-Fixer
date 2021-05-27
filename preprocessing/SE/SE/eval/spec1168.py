import numpy as np 

def function(x):

	a2 = x
	a9 = 5
	paths = []
	try:
		if a9 < 2:
			a2 = 8-x
			a9 = a9*3
			paths.append(1)
		else:
			a9 = a9+a2
			paths.append(2)
		if x < 3:
			x = 1-0
			paths.append(3)
		else:
			a2 = a2-5
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))