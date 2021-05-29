import numpy as np 

def function(x):

	e3 = 1
	x0 = 1
	x = x
	paths = []
	try:
		if x < 4:
			x0 = 3+1
			x0 = 6-x0
			paths.append(1)
		else:
			e3 = x-3
			paths.append(2)
		if e3 > 7:
			e3 = 0+e3
			x0 = 8/9
			paths.append(3)
		else:
			x = x-4
			x0 = x+e3
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))