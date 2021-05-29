import numpy as np 

def function(x):

	e6 = 2
	q7 = 8
	paths = []
	try:
		if e6 > 9:
			e6 = x-e6
			paths.append(1)
		else:
			x = 8+x
			e6 = 6*1
			x = x+2
			paths.append(2)
		if e6 > 0:
			x = x*9
			paths.append(3)
		else:
			e6 = 5*8
			q7 = q7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))