import numpy as np 

def function(x):

	t2 = 3
	e5 = 9
	x = x
	paths = []
	try:
		if t2 >= 3:
			t2 = t2*x
			paths.append(1)
		else:
			t2 = t2-x
			paths.append(2)
		if x > 6:
			e5 = e5/t2
			paths.append(3)
		else:
			x = x+3
			e5 = e5*6
			x = 6*t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))