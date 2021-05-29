import numpy as np 

def function(x):

	e3 = 2
	a9 = 3
	paths = []
	try:
		if e3 >= 7:
			x = e3/x
			e3 = 2/e3
			paths.append(1)
		else:
			x = e3/x
			paths.append(2)
		if e3 < 5:
			a9 = a9+a9
			e3 = e3+3
			paths.append(3)
		else:
			x = x+1
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