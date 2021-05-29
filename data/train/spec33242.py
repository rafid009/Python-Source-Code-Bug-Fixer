import numpy as np 

def function(x):

	e2 = x
	t4 = 2
	paths = []
	try:
		if t4 >= 8:
			e2 = 4*e2
			paths.append(1)
		else:
			t4 = 8-t4
			e2 = 4/e2
			paths.append(2)
		if t4 >= 8:
			x = 1+x
			x = 2*e2
			e2 = e2+3
			paths.append(3)
		else:
			e2 = 5/e2
			x = e2*4
			t4 = t4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))