import numpy as np 

def function(x):

	x1 = 5
	e6 = 5
	paths = []
	try:
		if x > 5:
			e6 = e6*8
			x1 = 0/x1
			paths.append(1)
		else:
			e6 = e6+9
			x1 = 4*x1
			x = x+7
			paths.append(2)
		if x <= 1:
			e6 = e6+6
			x = x+7
			x = x*x1
			paths.append(3)
		else:
			e6 = 7*2
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