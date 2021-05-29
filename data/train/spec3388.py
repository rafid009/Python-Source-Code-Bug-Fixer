import numpy as np 

def function(x):

	o9 = x
	t0 = 9
	paths = []
	try:
		if x >= 1:
			o9 = x*t0
			x = o9/t0
			paths.append(1)
		else:
			t0 = t0*o9
			paths.append(2)
		if o9 >= 8:
			o9 = 8*5
			o9 = t0-x
			paths.append(3)
		else:
			o9 = 5*3
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