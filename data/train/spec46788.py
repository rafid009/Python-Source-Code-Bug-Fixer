import numpy as np 

def function(x):

	e9 = x
	a8 = x
	paths = []
	try:
		if e9 <= 2:
			x = x+8
			x = x/e9
			paths.append(1)
		else:
			x = 5-0
			paths.append(2)
		if x >= 6:
			x = a8*x
			a8 = a8*7
			e9 = x+9
			paths.append(3)
		else:
			e9 = e9+6
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))