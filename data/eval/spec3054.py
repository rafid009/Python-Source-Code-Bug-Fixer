import numpy as np 

def function(x):

	e8 = 4
	t0 = 0
	paths = []
	try:
		if t0 < 9:
			x = 7+x
			e8 = t0-e8
			paths.append(1)
		else:
			t0 = 5/x
			e8 = 4/e8
			paths.append(2)
		if t0 <= 4:
			t0 = 6+t0
			paths.append(3)
		else:
			e8 = x*3
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