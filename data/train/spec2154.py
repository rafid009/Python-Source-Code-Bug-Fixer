import numpy as np 

def function(x):

	e3 = x
	t4 = 5
	x = 2
	paths = []
	try:
		if t4 < 6:
			e3 = t4/e3
			x = x-7
			e3 = 4*e3
			paths.append(1)
		else:
			t4 = 5-t4
			paths.append(2)
		if e3 > 2:
			t4 = t4+3
			e3 = e3-2
			paths.append(3)
		else:
			x = 6-5
			e3 = t4-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))