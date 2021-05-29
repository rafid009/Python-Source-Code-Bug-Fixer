import numpy as np 

def function(x):

	e3 = 5
	l1 = 9
	paths = []
	try:
		if l1 >= 8:
			l1 = 2*l1
			x = x+4
			paths.append(1)
		else:
			e3 = 9+e3
			paths.append(2)
		if x >= 9:
			e3 = 1*e3
			e3 = 0+3
			e3 = 5*e3
			paths.append(3)
		else:
			e3 = x+e3
			x = x*l1
			x = 8+x
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