import numpy as np 

def function(x):

	t0 = 2
	b8 = x
	paths = []
	try:
		if b8 < 8:
			x = t0/x
			x = x/6
			x = b8+5
			paths.append(1)
		else:
			x = b8-7
			paths.append(2)
		if x >= 4:
			b8 = 8-2
			x = x-b8
			paths.append(3)
		else:
			t0 = t0+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))