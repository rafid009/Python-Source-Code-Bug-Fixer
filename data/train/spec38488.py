import numpy as np 

def function(x):

	e9 = x
	u0 = x
	paths = []
	try:
		if e9 < 5:
			u0 = u0+e9
			e9 = u0-9
			paths.append(1)
		else:
			u0 = 2*u0
			e9 = e9/x
			u0 = 7+u0
			paths.append(2)
		if x > 9:
			x = x/4
			x = 6-x
			paths.append(3)
		else:
			e9 = x+e9
			u0 = 4/u0
			x = e9-u0
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))