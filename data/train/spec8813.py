import numpy as np 

def function(x):

	e0 = x
	g3 = x
	paths = []
	try:
		if e0 <= 2:
			e0 = e0+3
			x = 9*2
			paths.append(1)
		else:
			x = x-2
			e0 = 1/e0
			paths.append(2)
		if g3 <= 7:
			e0 = e0+9
			g3 = g3-3
			paths.append(3)
		else:
			e0 = 9*e0
			e0 = 3/e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))