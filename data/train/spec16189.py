import numpy as np 

def function(x):

	e9 = 4
	a1 = 5
	paths = []
	try:
		if e9 >= 9:
			x = x/6
			paths.append(1)
		else:
			e9 = e9+a1
			paths.append(2)
		if x < 5:
			a1 = a1/1
			paths.append(3)
		else:
			x = x/6
			a1 = e9*a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))