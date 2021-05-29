import numpy as np 

def function(x):

	e9 = 8
	e2 = 7
	paths = []
	try:
		if e2 < 1:
			e2 = 1+e9
			x = 7+x
			e2 = 8+5
			paths.append(1)
		else:
			e2 = e2/7
			e9 = x*x
			x = x+e2
			paths.append(2)
		if x <= 9:
			e9 = 9+e9
			paths.append(3)
		else:
			e2 = e2/1
			x = x-2
			e9 = e2-e9
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