import numpy as np 

def function(x):

	e9 = x
	x0 = x
	x = x
	paths = []
	try:
		if x0 >= 4:
			x = 1*6
			paths.append(1)
		else:
			x = x0*5
			paths.append(2)
		if e9 <= 5:
			e9 = e9+9
			x0 = x0-9
			paths.append(3)
		else:
			e9 = e9/e9
			e9 = 2/e9
			x0 = x0+4
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