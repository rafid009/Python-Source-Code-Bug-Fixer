import numpy as np 

def function(x):

	e7 = x
	t4 = 8
	paths = []
	try:
		if e7 > 9:
			e7 = 7-4
			paths.append(1)
		else:
			e7 = 1*x
			t4 = t4*3
			x = x-9
			paths.append(2)
		if t4 <= 0:
			x = x*e7
			e7 = 3/e7
			x = e7-x
			paths.append(3)
		else:
			x = e7+6
			t4 = t4-7
			t4 = 8+t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))