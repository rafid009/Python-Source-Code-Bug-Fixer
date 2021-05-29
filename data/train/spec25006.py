import numpy as np 

def function(x):

	t0 = x
	d7 = x
	paths = []
	try:
		if d7 < 7:
			t0 = 0-t0
			x = x+2
			paths.append(1)
		else:
			t0 = t0/t0
			t0 = 6/t0
			paths.append(2)
		if x > 0:
			d7 = 4/d7
			t0 = t0/d7
			paths.append(3)
		else:
			d7 = x-6
			t0 = t0-d7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		t0 = d7**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))