import numpy as np 

def function(x):

	e1 = x
	t0 = x
	paths = []
	try:
		if e1 > 3:
			x = 7-5
			e1 = e1+e1
			paths.append(1)
		else:
			t0 = t0-e1
			x = 8-1
			paths.append(2)
		if e1 > 7:
			e1 = 6+e1
			paths.append(3)
		else:
			t0 = t0-4
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))