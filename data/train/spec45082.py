import numpy as np 

def function(x):

	d0 = 4
	t7 = x
	paths = []
	try:
		if d0 > 9:
			x = x/7
			x = 0-x
			paths.append(1)
		else:
			d0 = 0/t7
			d0 = 3+d0
			paths.append(2)
		if t7 >= 0:
			d0 = 7/d0
			paths.append(3)
		else:
			t7 = x+t7
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