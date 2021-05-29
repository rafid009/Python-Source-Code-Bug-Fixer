import numpy as np 

def function(x):

	i5 = 0
	e9 = 4
	paths = []
	try:
		if e9 > 9:
			x = x-1
			i5 = i5+6
			paths.append(1)
		else:
			x = x*i5
			x = x-e9
			paths.append(2)
		if e9 <= 2:
			e9 = e9-3
			paths.append(3)
		else:
			i5 = i5/4
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