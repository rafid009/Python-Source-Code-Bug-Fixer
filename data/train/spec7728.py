import numpy as np 

def function(x):

	e8 = x
	i9 = 2
	paths = []
	try:
		if x <= 8:
			x = i9/x
			e8 = 3+e8
			e8 = e8+2
			paths.append(1)
		else:
			e8 = e8*e8
			e8 = e8-4
			e8 = 2*e8
			paths.append(2)
		if x <= 4:
			i9 = i9*0
			e8 = 2*3
			paths.append(3)
		else:
			i9 = 4-7
			e8 = e8/e8
			e8 = e8+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))