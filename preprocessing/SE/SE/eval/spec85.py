import numpy as np 

def function(x):

	e1 = 5
	e7 = x
	paths = []
	try:
		if x < 5:
			e1 = 3*e1
			e1 = e1-0
			paths.append(1)
		else:
			x = 2+8
			x = 0/x
			paths.append(2)
		if x < 3:
			x = e7+x
			paths.append(3)
		else:
			x = 2-x
			e7 = 1*e7
			e7 = e7-4
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e1 = e7**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))