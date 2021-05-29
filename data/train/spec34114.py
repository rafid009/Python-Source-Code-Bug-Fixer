import numpy as np 

def function(x):

	e9 = 7
	u4 = 5
	paths = []
	try:
		if u4 >= 6:
			e9 = 6*e9
			x = x*8
			paths.append(1)
		else:
			e9 = 6/e9
			paths.append(2)
		if x <= 7:
			u4 = u4-x
			paths.append(3)
		else:
			e9 = 4-u4
			e9 = e9/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))