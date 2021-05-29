import numpy as np 

def function(x):

	a4 = x
	r9 = 2
	paths = []
	try:
		if r9 <= 2:
			a4 = a4-8
			x = r9-3
			r9 = r9*1
			paths.append(1)
		else:
			x = x-x
			a4 = 5+a4
			a4 = 1*x
			paths.append(2)
		if a4 >= 5:
			a4 = a4*4
			a4 = a4*x
			paths.append(3)
		else:
			a4 = 8+a4
			r9 = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))