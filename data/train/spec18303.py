import numpy as np 

def function(x):

	e6 = x
	x3 = x
	paths = []
	try:
		if x3 >= 1:
			x = x/x
			x = 5/x
			paths.append(1)
		else:
			x3 = x*0
			x3 = x*6
			x3 = 2-x3
			paths.append(2)
		if x > 4:
			e6 = e6*3
			e6 = e6*e6
			paths.append(3)
		else:
			e6 = 7-e6
			e6 = x/4
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