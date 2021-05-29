import numpy as np 

def function(x):

	t0 = x
	k6 = x
	x = 7
	paths = []
	try:
		if t0 < 6:
			x = x*x
			t0 = t0-3
			x = 8-x
			paths.append(1)
		else:
			t0 = x/9
			x = k6+t0
			paths.append(2)
		if k6 >= 0:
			x = t0+2
			paths.append(3)
		else:
			t0 = t0/3
			x = 4*t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))