import numpy as np 

def function(x):

	t0 = x
	t4 = 8
	paths = []
	try:
		if x < 8:
			x = 0-9
			t4 = t4*t0
			paths.append(1)
		else:
			x = 1+6
			paths.append(2)
		if t0 < 1:
			t4 = t4/t4
			paths.append(3)
		else:
			x = x*9
			t0 = t0*3
			t4 = t4/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))