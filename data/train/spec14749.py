import numpy as np 

def function(x):

	e5 = 7
	paths = []
	try:
		if e5 < 9:
			e5 = x/9
			paths.append(1)
		else:
			x = x/8
			e5 = e5+x
			e5 = 6+3
			paths.append(2)
		if x >= 0:
			e5 = 0*e5
			x = 4-x
			paths.append(3)
		else:
			e5 = 6-1
			x = 4/6
			e5 = 0+e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))