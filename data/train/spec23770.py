import numpy as np 

def function(x):

	e6 = x
	u4 = 7
	x = x
	paths = []
	try:
		if u4 > 2:
			e6 = e6+6
			paths.append(1)
		else:
			e6 = e6*3
			u4 = 9*u4
			e6 = 1/e6
			paths.append(2)
		if u4 >= 3:
			e6 = 0+e6
			u4 = e6/8
			paths.append(3)
		else:
			x = x-x
			e6 = e6+8
			x = 5-u4
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))