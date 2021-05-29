import numpy as np 

def function(x):

	a8 = x
	t6 = x
	paths = []
	try:
		if a8 < 8:
			x = x+t6
			a8 = a8/3
			t6 = t6-2
			paths.append(1)
		else:
			t6 = t6+4
			paths.append(2)
		if t6 > 2:
			x = 6+4
			t6 = 8+5
			x = 8+4
			paths.append(3)
		else:
			a8 = a8-1
			a8 = a8/2
			t6 = t6*a8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))