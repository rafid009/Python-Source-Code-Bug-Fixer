import numpy as np 

def function(x):

	y3 = x
	e2 = x
	paths = []
	try:
		if y3 < 6:
			x = 4+e2
			e2 = e2/e2
			y3 = x*y3
			paths.append(1)
		else:
			y3 = 7-y3
			y3 = 5-8
			paths.append(2)
		if y3 > 5:
			e2 = y3+e2
			paths.append(3)
		else:
			y3 = y3/7
			e2 = 1*6
			x = e2+e2
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		e2 = y3**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))