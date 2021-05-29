import numpy as np 

def function(x):

	t6 = 9
	d6 = x
	paths = []
	try:
		if d6 >= 9:
			d6 = 6*d6
			x = 7/x
			paths.append(1)
		else:
			t6 = x-t6
			t6 = 3/t6
			t6 = 4+t6
			paths.append(2)
		if t6 <= 8:
			d6 = 4-d6
			d6 = 4-d6
			d6 = 6/8
			paths.append(3)
		else:
			x = x-d6
			t6 = 0/t6
			d6 = d6-3
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