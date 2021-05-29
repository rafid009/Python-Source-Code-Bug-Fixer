import numpy as np 

def function(x):

	t2 = x
	e8 = 3
	paths = []
	try:
		if t2 < 3:
			x = x*e8
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if x <= 6:
			t2 = t2+6
			e8 = 7+e8
			paths.append(3)
		else:
			e8 = 5*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))