import numpy as np 

def function(x):

	e0 = x
	a7 = 5
	paths = []
	try:
		if x <= 5:
			e0 = 4-5
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if e0 >= 3:
			e0 = e0+8
			a7 = e0+a7
			paths.append(3)
		else:
			a7 = 2/a7
			a7 = e0+a7
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))