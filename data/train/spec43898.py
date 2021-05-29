import numpy as np 

def function(x):

	d0 = x
	t0 = x
	paths = []
	try:
		if t0 <= 6:
			x = x+d0
			t0 = x+3
			d0 = 6/6
			paths.append(1)
		else:
			d0 = x-7
			t0 = 5-7
			paths.append(2)
		if x < 8:
			d0 = d0-2
			d0 = d0-x
			t0 = x-t0
			paths.append(3)
		else:
			d0 = 5*x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))