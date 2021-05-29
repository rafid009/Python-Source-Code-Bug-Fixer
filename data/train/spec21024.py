import numpy as np 

def function(x):

	a2 = 6
	b7 = 7
	paths = []
	try:
		if x >= 9:
			a2 = 9+a2
			x = 5*x
			b7 = 1/b7
			paths.append(1)
		else:
			a2 = b7/a2
			a2 = a2/6
			a2 = 3*a2
			paths.append(2)
		if x <= 9:
			b7 = b7-x
			a2 = 8*a2
			a2 = a2+7
			paths.append(3)
		else:
			a2 = 0+b7
			x = x/x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		a2 = b7**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))