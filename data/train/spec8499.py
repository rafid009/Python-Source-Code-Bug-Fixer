import numpy as np 

def function(x):

	a9 = 9
	a8 = 7
	paths = []
	try:
		if a8 >= 0:
			a9 = a8/3
			paths.append(1)
		else:
			a8 = 9*a8
			a8 = 4+5
			paths.append(2)
		if a8 > 0:
			x = 2+x
			x = x-0
			a9 = a9-a8
			paths.append(3)
		else:
			a9 = a9-x
			x = 9+3
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))