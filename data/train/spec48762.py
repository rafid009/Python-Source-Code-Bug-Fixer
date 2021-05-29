import numpy as np 

def function(x):

	a8 = 5
	d1 = x
	paths = []
	try:
		if a8 <= 4:
			d1 = x-d1
			a8 = 2+x
			d1 = a8-d1
			paths.append(1)
		else:
			d1 = 3*d1
			x = x-8
			paths.append(2)
		if a8 < 1:
			x = x+d1
			a8 = 8/x
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))