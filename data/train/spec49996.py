import numpy as np 

def function(x):

	e4 = x
	j9 = 3
	paths = []
	try:
		if e4 <= 1:
			j9 = 1-3
			x = x+9
			x = x-9
			paths.append(1)
		else:
			j9 = 1+j9
			paths.append(2)
		if x < 7:
			x = x+6
			paths.append(3)
		else:
			j9 = e4/j9
			x = 9/9
			x = x*e4
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