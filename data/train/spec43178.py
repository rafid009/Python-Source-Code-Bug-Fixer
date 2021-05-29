import numpy as np 

def function(x):

	e8 = 9
	n8 = 1
	paths = []
	try:
		if e8 >= 0:
			e8 = 0*e8
			e8 = x+e8
			n8 = n8-7
			paths.append(1)
		else:
			x = n8/n8
			n8 = n8+6
			e8 = x*x
			paths.append(2)
		if e8 >= 1:
			e8 = e8-5
			x = x+9
			x = 8*7
			paths.append(3)
		else:
			e8 = e8-e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))