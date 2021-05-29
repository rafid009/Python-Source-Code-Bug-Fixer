import numpy as np 

def function(x):

	x3 = 2
	t8 = x
	paths = []
	try:
		if x <= 7:
			x3 = x+x3
			paths.append(1)
		else:
			x = x-9
			x = 2-x
			t8 = t8-t8
			paths.append(2)
		if x <= 8:
			t8 = t8-2
			x = x3+x
			paths.append(3)
		else:
			t8 = 1+t8
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))