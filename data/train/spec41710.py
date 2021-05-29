import numpy as np 

def function(x):

	e5 = x
	u1 = x
	paths = []
	try:
		if e5 <= 1:
			u1 = 7*u1
			paths.append(1)
		else:
			x = 4*x
			e5 = 8+7
			x = x+x
			paths.append(2)
		if e5 < 5:
			u1 = 7/3
			x = 4+5
			u1 = 7/u1
			paths.append(3)
		else:
			x = 4/x
			x = x-e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))