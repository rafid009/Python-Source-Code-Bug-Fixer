import numpy as np 

def function(x):

	e7 = 7
	a3 = 5
	paths = []
	try:
		if a3 <= 3:
			e7 = 9*7
			a3 = x/7
			a3 = a3-1
			paths.append(1)
		else:
			x = x+9
			e7 = 8/3
			e7 = a3+4
			paths.append(2)
		if x < 1:
			e7 = 2+e7
			e7 = 7*2
			e7 = 8*e7
			paths.append(3)
		else:
			a3 = a3-a3
			e7 = e7-e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))