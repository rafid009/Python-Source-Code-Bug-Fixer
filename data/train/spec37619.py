import numpy as np 

def function(x):

	t8 = 5
	n0 = 8
	x = x
	paths = []
	try:
		if n0 < 6:
			x = t8-1
			n0 = x/6
			paths.append(1)
		else:
			t8 = 0/t8
			paths.append(2)
		if n0 <= 5:
			n0 = n0*2
			paths.append(3)
		else:
			x = x-6
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