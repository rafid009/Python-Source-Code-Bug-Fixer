import numpy as np 

def function(x):

	t0 = 3
	b7 = x
	paths = []
	try:
		if t0 >= 2:
			t0 = t0*1
			x = b7-1
			paths.append(1)
		else:
			t0 = 8/4
			b7 = t0*4
			paths.append(2)
		if t0 >= 0:
			x = x-5
			t0 = x*4
			paths.append(3)
		else:
			x = x-4
			x = x*9
			t0 = b7-t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))