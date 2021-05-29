import numpy as np 

def function(x):

	d3 = x
	t0 = x
	x = x
	paths = []
	try:
		if t0 > 0:
			x = x*4
			t0 = 3/2
			paths.append(1)
		else:
			x = x*d3
			paths.append(2)
		if t0 < 5:
			t0 = t0/8
			d3 = 9*d3
			paths.append(3)
		else:
			t0 = t0/2
			x = x-8
			t0 = 1*8
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		t0 = d3**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))