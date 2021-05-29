import numpy as np 

def function(x):

	a9 = x
	a5 = 5
	paths = []
	try:
		if a9 >= 1:
			x = 9-5
			x = 3+x
			paths.append(1)
		else:
			x = a9/a5
			a9 = a9/4
			x = 3+a9
			paths.append(2)
		if a5 <= 0:
			a5 = 9+7
			a5 = a5*a9
			x = x+x
			paths.append(3)
		else:
			a5 = a9*7
			a9 = a5+6
			a9 = 7/a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))