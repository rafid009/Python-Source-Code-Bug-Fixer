import numpy as np 

def function(x):

	y3 = x
	e7 = x
	x = 4
	paths = []
	try:
		if x >= 5:
			e7 = e7*y3
			e7 = 4/e7
			y3 = y3/5
			paths.append(1)
		else:
			x = 7+1
			y3 = 7-5
			paths.append(2)
		if x <= 4:
			e7 = 4/y3
			paths.append(3)
		else:
			e7 = e7/6
			y3 = 5/y3
			y3 = y3/9
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))