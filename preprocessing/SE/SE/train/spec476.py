import numpy as np 

def function(x):

	e0 = 8
	u3 = x
	paths = []
	try:
		if e0 < 4:
			u3 = u3*7
			e0 = 8-5
			x = x+u3
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if e0 < 4:
			e0 = 2/e0
			u3 = u3-9
			x = u3*9
			paths.append(3)
		else:
			e0 = e0*e0
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