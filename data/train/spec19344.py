import numpy as np 

def function(x):

	t2 = x
	k2 = 4
	paths = []
	try:
		if x <= 9:
			x = x-2
			k2 = k2/1
			k2 = k2+4
			paths.append(1)
		else:
			x = t2/9
			k2 = 4*k2
			paths.append(2)
		if x < 9:
			k2 = k2/x
			paths.append(3)
		else:
			k2 = 3/k2
			k2 = k2-5
			t2 = t2*t2
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