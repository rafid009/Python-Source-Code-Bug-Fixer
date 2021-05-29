import numpy as np 

def function(x):

	x2 = x
	e5 = x
	paths = []
	try:
		if x2 >= 8:
			x = e5/1
			x = x+3
			paths.append(1)
		else:
			x2 = x2-2
			x = x+x
			x2 = 2/2
			paths.append(2)
		if x > 8:
			x = 4+2
			paths.append(3)
		else:
			e5 = e5-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))