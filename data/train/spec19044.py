import numpy as np 

def function(x):

	v0 = x
	e7 = 5
	paths = []
	try:
		if v0 >= 7:
			e7 = 3-4
			paths.append(1)
		else:
			v0 = 6*v0
			v0 = e7/v0
			x = x*2
			paths.append(2)
		if x >= 6:
			v0 = 5*1
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))