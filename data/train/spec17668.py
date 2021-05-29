import numpy as np 

def function(x):

	o5 = 9
	t0 = 4
	paths = []
	try:
		if t0 < 7:
			t0 = t0+0
			paths.append(1)
		else:
			t0 = 0*7
			t0 = t0+5
			paths.append(2)
		if x < 5:
			o5 = 8+o5
			paths.append(3)
		else:
			x = o5+0
			t0 = 1-t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))