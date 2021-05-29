import numpy as np 

def function(x):

	e1 = x
	o7 = 3
	paths = []
	try:
		if e1 > 1:
			e1 = e1/4
			e1 = e1+o7
			e1 = x+e1
			paths.append(1)
		else:
			e1 = 6/6
			e1 = 7*3
			paths.append(2)
		if x <= 4:
			o7 = o7+8
			paths.append(3)
		else:
			e1 = e1+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))