import numpy as np 

def function(x):

	v7 = 0
	e5 = x
	paths = []
	try:
		if v7 >= 7:
			x = x/8
			paths.append(1)
		else:
			e5 = x/x
			v7 = 6+8
			paths.append(2)
		if x > 3:
			e5 = e5+x
			paths.append(3)
		else:
			e5 = e5*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))