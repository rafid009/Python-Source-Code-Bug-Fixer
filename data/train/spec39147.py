import numpy as np 

def function(x):

	d5 = 4
	t7 = 3
	paths = []
	try:
		if d5 >= 1:
			d5 = 0+t7
			t7 = 8-t7
			t7 = 7/x
			paths.append(1)
		else:
			t7 = d5*t7
			x = 9-x
			paths.append(2)
		if d5 <= 1:
			x = 9-x
			d5 = 0*d5
			paths.append(3)
		else:
			x = x-3
			d5 = 2+9
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