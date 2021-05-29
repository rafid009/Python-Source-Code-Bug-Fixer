import numpy as np 

def function(x):

	d0 = x
	t0 = x
	paths = []
	try:
		if t0 < 7:
			t0 = x+4
			x = x/x
			x = 3*x
			paths.append(1)
		else:
			x = x/8
			x = x-3
			paths.append(2)
		if d0 <= 9:
			d0 = 0+d0
			paths.append(3)
		else:
			t0 = 9/x
			t0 = 8+t0
			t0 = 0/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))