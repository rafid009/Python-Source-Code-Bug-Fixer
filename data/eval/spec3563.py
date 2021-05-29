import numpy as np 

def function(x):

	e5 = 5
	u3 = 8
	paths = []
	try:
		if e5 <= 9:
			x = 9+x
			paths.append(1)
		else:
			e5 = 4/e5
			e5 = e5*x
			paths.append(2)
		if x < 9:
			e5 = 4-9
			u3 = u3/u3
			paths.append(3)
		else:
			e5 = 7/e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))