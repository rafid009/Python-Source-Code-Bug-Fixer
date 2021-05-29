import numpy as np 

def function(x):

	t4 = 7
	k0 = x
	paths = []
	try:
		if k0 > 7:
			t4 = t4-0
			paths.append(1)
		else:
			k0 = 2*t4
			k0 = x*k0
			paths.append(2)
		if t4 > 7:
			x = t4/k0
			paths.append(3)
		else:
			t4 = 3*t4
			x = 5-x
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