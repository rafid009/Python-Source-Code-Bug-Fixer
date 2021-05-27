import numpy as np 

def function(x):

	n9 = x
	t8 = 8
	paths = []
	try:
		if x < 2:
			n9 = n9+n9
			n9 = x-3
			paths.append(1)
		else:
			x = 3+4
			paths.append(2)
		if t8 > 4:
			t8 = n9*t8
			x = 3+x
			n9 = 4+n9
			paths.append(3)
		else:
			n9 = 8/6
			t8 = n9/t8
			n9 = 7/n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))