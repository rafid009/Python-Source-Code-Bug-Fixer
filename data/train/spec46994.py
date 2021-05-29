import numpy as np 

def function(x):

	a6 = x
	q8 = x
	paths = []
	try:
		if q8 < 6:
			x = 5+x
			a6 = a6/a6
			a6 = a6/8
			paths.append(1)
		else:
			q8 = a6/q8
			x = x+3
			paths.append(2)
		if q8 >= 3:
			a6 = a6-q8
			x = 7*5
			paths.append(3)
		else:
			a6 = a6-x
			q8 = q8-q8
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))