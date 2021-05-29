import numpy as np 

def function(x):

	e1 = x
	x3 = 5
	paths = []
	try:
		if x3 < 8:
			x3 = 5+2
			x = x/7
			paths.append(1)
		else:
			e1 = x3/e1
			e1 = 2-e1
			x3 = x3-6
			paths.append(2)
		if x >= 5:
			x3 = e1-x3
			e1 = 8*0
			x = x/8
			paths.append(3)
		else:
			x = 3/x
			x3 = x3*x3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))