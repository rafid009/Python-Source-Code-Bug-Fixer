import numpy as np 

def function(x):

	v3 = x
	e2 = 8
	paths = []
	try:
		if e2 > 2:
			x = x/7
			paths.append(1)
		else:
			v3 = 3/v3
			x = x*1
			x = x/4
			paths.append(2)
		if v3 >= 9:
			e2 = x+3
			paths.append(3)
		else:
			e2 = 2*e2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))