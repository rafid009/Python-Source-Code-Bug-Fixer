import numpy as np 

def function(x):

	e7 = 9
	f7 = x
	paths = []
	try:
		if x < 1:
			e7 = f7+e7
			paths.append(1)
		else:
			x = x*x
			e7 = e7/1
			paths.append(2)
		if x <= 8:
			x = x-1
			paths.append(3)
		else:
			e7 = 5+f7
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