import numpy as np 

def function(x):

	e9 = 6
	v5 = 8
	paths = []
	try:
		if x >= 9:
			v5 = v5-5
			x = 5+9
			x = 0/4
			paths.append(1)
		else:
			v5 = 2-0
			paths.append(2)
		if x >= 6:
			v5 = 5*1
			paths.append(3)
		else:
			e9 = e9-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))