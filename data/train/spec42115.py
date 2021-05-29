import numpy as np 

def function(x):

	t0 = 5
	j1 = 0
	paths = []
	try:
		if t0 < 8:
			x = 3-x
			paths.append(1)
		else:
			x = x/t0
			j1 = j1+0
			x = 2/x
			paths.append(2)
		if x < 9:
			t0 = 4*t0
			paths.append(3)
		else:
			t0 = 1/t0
			t0 = 2/1
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