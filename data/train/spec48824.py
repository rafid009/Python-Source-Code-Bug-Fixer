import numpy as np 

def function(x):

	v8 = 7
	t0 = x
	paths = []
	try:
		if x >= 3:
			v8 = 3+v8
			x = 1+x
			paths.append(1)
		else:
			t0 = t0+t0
			t0 = 2*t0
			paths.append(2)
		if x >= 7:
			x = 8/x
			v8 = 2+v8
			v8 = x/v8
			paths.append(3)
		else:
			v8 = 8+v8
			t0 = v8*t0
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))