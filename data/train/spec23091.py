import numpy as np 

def function(x):

	p9 = x
	e4 = 9
	paths = []
	try:
		if p9 >= 2:
			x = 3*4
			paths.append(1)
		else:
			x = e4/x
			paths.append(2)
		if p9 < 9:
			x = x+e4
			e4 = e4*7
			paths.append(3)
		else:
			x = x/9
			e4 = 8+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))