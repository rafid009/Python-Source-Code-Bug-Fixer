import numpy as np 

def function(x):

	t0 = x
	k7 = x
	paths = []
	try:
		if x <= 0:
			x = x-0
			k7 = k7*k7
			paths.append(1)
		else:
			x = 6-k7
			paths.append(2)
		if x >= 5:
			k7 = 8*k7
			t0 = t0*4
			paths.append(3)
		else:
			t0 = t0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))