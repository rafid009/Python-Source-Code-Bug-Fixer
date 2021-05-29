import numpy as np 

def function(x):

	e7 = 3
	a9 = x
	paths = []
	try:
		if e7 > 6:
			a9 = 5+a9
			a9 = a9/a9
			e7 = e7/1
			paths.append(1)
		else:
			a9 = a9+e7
			paths.append(2)
		if x > 1:
			x = x-e7
			e7 = x/e7
			a9 = 3/a9
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))