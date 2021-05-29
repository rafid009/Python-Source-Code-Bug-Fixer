import numpy as np 

def function(x):

	v6 = 6
	e1 = 5
	paths = []
	try:
		if e1 > 3:
			e1 = 4+v6
			e1 = e1*e1
			paths.append(1)
		else:
			e1 = e1/e1
			paths.append(2)
		if v6 >= 1:
			e1 = 2/e1
			x = 9-x
			v6 = v6-1
			paths.append(3)
		else:
			v6 = 6-v6
			e1 = e1-7
			e1 = 7-e1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))