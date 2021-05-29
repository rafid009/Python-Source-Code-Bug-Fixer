import numpy as np 

def function(x):

	x5 = 0
	t0 = x
	paths = []
	try:
		if x > 4:
			x = 6+7
			t0 = t0-5
			paths.append(1)
		else:
			x5 = 0-x5
			t0 = 2-x5
			x5 = x5+5
			paths.append(2)
		if t0 >= 4:
			x5 = x5-1
			x = x5+5
			paths.append(3)
		else:
			t0 = t0*t0
			t0 = 8+t0
			x = x*t0
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))