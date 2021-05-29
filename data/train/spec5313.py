import numpy as np 

def function(x):

	e4 = x
	d9 = 2
	paths = []
	try:
		if x < 8:
			e4 = e4-2
			d9 = 5/2
			x = x*6
			paths.append(1)
		else:
			x = e4/e4
			e4 = 9/d9
			paths.append(2)
		if x <= 5:
			d9 = d9/1
			e4 = e4+6
			paths.append(3)
		else:
			e4 = 7*e4
			d9 = d9/5
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