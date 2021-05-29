import numpy as np 

def function(x):

	q8 = x
	e8 = x
	paths = []
	try:
		if q8 > 5:
			q8 = 2-q8
			e8 = e8/e8
			paths.append(1)
		else:
			q8 = q8+q8
			q8 = 2-8
			x = 6*x
			paths.append(2)
		if q8 > 4:
			q8 = e8*x
			x = 9-3
			x = x+9
			paths.append(3)
		else:
			e8 = e8-q8
			x = 5+x
			x = x-e8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))