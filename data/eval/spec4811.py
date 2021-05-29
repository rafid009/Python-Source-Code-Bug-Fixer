import numpy as np 

def function(x):

	d2 = 4
	t0 = x
	paths = []
	try:
		if d2 >= 2:
			t0 = d2/3
			d2 = d2*1
			x = 8-x
			paths.append(1)
		else:
			x = 1+1
			d2 = 3/d2
			paths.append(2)
		if x >= 1:
			d2 = d2-2
			d2 = 6+d2
			paths.append(3)
		else:
			t0 = t0-x
			d2 = 9*t0
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