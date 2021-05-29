import numpy as np 

def function(x):

	a7 = x
	t2 = x
	x = x
	paths = []
	try:
		if a7 > 8:
			x = 9-t2
			x = 7+x
			x = x-x
			paths.append(1)
		else:
			t2 = t2-6
			paths.append(2)
		if a7 > 1:
			t2 = t2/7
			paths.append(3)
		else:
			a7 = a7-2
			t2 = x-0
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