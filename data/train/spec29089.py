import numpy as np 

def function(x):

	t8 = 1
	e2 = 1
	paths = []
	try:
		if t8 > 9:
			e2 = e2*5
			x = 1-8
			paths.append(1)
		else:
			x = t8*x
			t8 = 0-t8
			e2 = e2*e2
			paths.append(2)
		if t8 < 1:
			e2 = e2*t8
			x = x*8
			e2 = 5+e2
			paths.append(3)
		else:
			t8 = 0/5
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