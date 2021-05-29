import numpy as np 

def function(x):

	e7 = x
	r7 = 3
	paths = []
	try:
		if e7 < 0:
			e7 = 1*5
			paths.append(1)
		else:
			e7 = e7/8
			e7 = 2-e7
			paths.append(2)
		if x < 1:
			e7 = 8/e7
			x = 6+8
			e7 = r7-r7
			paths.append(3)
		else:
			r7 = r7/5
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