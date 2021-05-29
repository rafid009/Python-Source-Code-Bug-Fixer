import numpy as np 

def function(x):

	e0 = x
	f7 = 7
	paths = []
	try:
		if x > 4:
			x = x-e0
			paths.append(1)
		else:
			e0 = e0-0
			x = x-e0
			paths.append(2)
		if f7 > 3:
			f7 = f7+0
			x = 0+e0
			paths.append(3)
		else:
			x = 0+x
			e0 = 5-e0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))