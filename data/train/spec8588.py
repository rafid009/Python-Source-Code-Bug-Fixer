import numpy as np 

def function(x):

	t9 = x
	e9 = 2
	paths = []
	try:
		if x > 1:
			t9 = t9*7
			paths.append(1)
		else:
			x = 0+x
			t9 = 9-t9
			paths.append(2)
		if x > 2:
			e9 = t9+5
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))