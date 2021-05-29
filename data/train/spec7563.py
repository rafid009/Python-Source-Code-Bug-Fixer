import numpy as np 

def function(x):

	t0 = x
	r6 = 1
	paths = []
	try:
		if t0 < 2:
			r6 = t0/2
			paths.append(1)
		else:
			x = r6-x
			r6 = 8/2
			paths.append(2)
		if t0 < 7:
			t0 = t0-8
			t0 = 9+0
			paths.append(3)
		else:
			t0 = t0/8
			x = 3/9
			t0 = t0*t0
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))