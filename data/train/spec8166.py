import numpy as np 

def function(x):

	e0 = x
	e4 = x
	paths = []
	try:
		if e0 < 5:
			e4 = e4+7
			e0 = x-e0
			e0 = 3+0
			paths.append(1)
		else:
			e0 = e0*x
			paths.append(2)
		if x > 7:
			e4 = e4+e4
			e4 = x+e4
			e0 = e0+x
			paths.append(3)
		else:
			e4 = e4-4
			x = 5-1
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))