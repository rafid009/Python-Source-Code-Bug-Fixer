import numpy as np 

def function(x):

	a5 = x
	e4 = 9
	paths = []
	try:
		if a5 < 6:
			e4 = x+x
			a5 = 7*7
			paths.append(1)
		else:
			x = a5-a5
			x = 3+6
			paths.append(2)
		if x <= 7:
			a5 = 9-8
			paths.append(3)
		else:
			x = a5/a5
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))