import numpy as np 

def function(x):

	a9 = x
	e4 = x
	paths = []
	try:
		if e4 <= 9:
			e4 = 6/a9
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if a9 >= 8:
			a9 = a9-e4
			x = x-a9
			e4 = 5-e4
			paths.append(3)
		else:
			x = x/6
			x = x/9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		e4 = a9**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))