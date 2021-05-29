import numpy as np 

def function(x):

	e8 = 5
	x4 = 9
	paths = []
	try:
		if e8 >= 8:
			e8 = e8/1
			paths.append(1)
		else:
			x = x/9
			x = x*x4
			paths.append(2)
		if x4 > 1:
			x4 = x4-8
			paths.append(3)
		else:
			x = x+0
			x4 = e8*x4
			x4 = x*x
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