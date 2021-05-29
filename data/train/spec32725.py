import numpy as np 

def function(x):

	a8 = 3
	t0 = x
	paths = []
	try:
		if x <= 4:
			t0 = a8+x
			paths.append(1)
		else:
			t0 = t0-1
			x = 5*a8
			a8 = a8/a8
			paths.append(2)
		if x < 4:
			t0 = 8+t0
			t0 = 2+4
			paths.append(3)
		else:
			t0 = 7/4
			x = x-t0
			x = x+7
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