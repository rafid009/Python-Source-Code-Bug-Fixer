import numpy as np 

def function(x):

	x4 = x
	e6 = x
	x = 8
	paths = []
	try:
		if e6 <= 7:
			x4 = 6-1
			e6 = e6*x4
			x4 = x4/e6
			paths.append(1)
		else:
			e6 = e6-9
			paths.append(2)
		if x >= 7:
			e6 = e6/8
			paths.append(3)
		else:
			x4 = 8/6
			x = x4-7
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x4 = e6**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))