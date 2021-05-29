import numpy as np 

def function(x):

	e0 = x
	e9 = 3
	paths = []
	try:
		if e9 > 8:
			e9 = 6*e9
			e9 = 0+e0
			paths.append(1)
		else:
			e0 = e0/5
			e0 = e0/e9
			e9 = e0/e0
			paths.append(2)
		if x < 8:
			e9 = 5-e0
			paths.append(3)
		else:
			e9 = e9*3
			e0 = e0*e9
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