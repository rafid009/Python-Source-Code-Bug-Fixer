import numpy as np 

def function(x):

	e7 = x
	t0 = x
	paths = []
	try:
		if t0 >= 0:
			t0 = e7+9
			e7 = e7-e7
			paths.append(1)
		else:
			t0 = t0*e7
			paths.append(2)
		if t0 >= 9:
			x = t0+1
			paths.append(3)
		else:
			x = 3*9
			t0 = t0+e7
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		e7 = t0**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))