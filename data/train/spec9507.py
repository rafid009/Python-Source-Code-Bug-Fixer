import numpy as np 

def function(x):

	v1 = x
	e5 = 5
	paths = []
	try:
		if v1 >= 6:
			e5 = e5-e5
			paths.append(1)
		else:
			v1 = v1-e5
			v1 = v1+3
			paths.append(2)
		if v1 < 4:
			v1 = 0-v1
			paths.append(3)
		else:
			x = v1/8
			v1 = x+5
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