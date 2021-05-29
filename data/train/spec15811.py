import numpy as np 

def function(x):

	t2 = x
	t0 = 6
	paths = []
	try:
		if t0 < 2:
			t0 = t0-t0
			x = x-7
			paths.append(1)
		else:
			t0 = 5+x
			t0 = t0/9
			t0 = t0/6
			paths.append(2)
		if t2 > 5:
			x = t0*5
			t2 = t0+t2
			paths.append(3)
		else:
			x = 2-x
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