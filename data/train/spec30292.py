import numpy as np 

def function(x):

	j9 = x
	a9 = 8
	paths = []
	try:
		if j9 <= 4:
			j9 = a9+0
			paths.append(1)
		else:
			j9 = j9-4
			paths.append(2)
		if j9 <= 5:
			j9 = 0+j9
			j9 = j9*a9
			paths.append(3)
		else:
			j9 = 3+j9
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))