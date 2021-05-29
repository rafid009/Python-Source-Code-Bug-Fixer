import numpy as np 

def function(x):

	a3 = 5
	a7 = x
	x = 9
	paths = []
	try:
		if x > 3:
			x = 9-x
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if a7 <= 8:
			a7 = 6*a7
			a7 = a7+3
			a7 = a7+a7
			paths.append(3)
		else:
			x = x*x
			x = 6*a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))