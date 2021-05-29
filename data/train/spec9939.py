import numpy as np 

def function(x):

	r9 = x
	t0 = 0
	paths = []
	try:
		if r9 > 0:
			r9 = 6+0
			paths.append(1)
		else:
			r9 = 6+1
			r9 = r9-2
			paths.append(2)
		if t0 < 7:
			t0 = t0-r9
			paths.append(3)
		else:
			x = x/3
			r9 = r9+5
			x = 8-x
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