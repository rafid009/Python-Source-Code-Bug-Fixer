import numpy as np 

def function(x):

	y3 = 3
	e3 = 7
	paths = []
	try:
		if y3 <= 9:
			y3 = 2-y3
			y3 = y3/y3
			y3 = 9-2
			paths.append(1)
		else:
			y3 = x/e3
			e3 = e3-e3
			e3 = e3+8
			paths.append(2)
		if x <= 8:
			y3 = y3+0
			e3 = 5-e3
			y3 = e3*y3
			paths.append(3)
		else:
			e3 = 1+e3
			y3 = y3*x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))