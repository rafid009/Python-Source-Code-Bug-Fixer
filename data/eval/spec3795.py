import numpy as np 

def function(x):

	y1 = 7
	e5 = x
	paths = []
	try:
		if e5 < 1:
			y1 = y1+7
			paths.append(1)
		else:
			y1 = 2*y1
			y1 = 7/9
			y1 = e5*y1
			paths.append(2)
		if x > 4:
			e5 = 6+e5
			paths.append(3)
		else:
			y1 = e5/e5
			x = 8+x
			x = x*6
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