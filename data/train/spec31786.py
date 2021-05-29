import numpy as np 

def function(x):

	t0 = 0
	e1 = x
	x = x
	paths = []
	try:
		if t0 < 2:
			e1 = e1-5
			x = x/x
			e1 = 9+e1
			paths.append(1)
		else:
			t0 = 4+5
			paths.append(2)
		if t0 >= 7:
			t0 = 0/6
			t0 = 3-e1
			paths.append(3)
		else:
			x = 0*7
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))