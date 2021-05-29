import numpy as np 

def function(x):

	e7 = x
	v1 = x
	paths = []
	try:
		if v1 >= 6:
			v1 = v1-8
			v1 = e7/e7
			e7 = e7*x
			paths.append(1)
		else:
			e7 = e7+3
			x = x-5
			paths.append(2)
		if x > 7:
			e7 = 2/e7
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		e7 = v1**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))