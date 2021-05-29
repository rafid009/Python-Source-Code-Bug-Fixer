import numpy as np 

def function(x):

	d4 = 5
	a1 = 1
	paths = []
	try:
		if d4 >= 1:
			x = x+7
			d4 = d4-6
			paths.append(1)
		else:
			a1 = d4*6
			a1 = a1-d4
			paths.append(2)
		if a1 <= 4:
			x = x/7
			a1 = 5/a1
			paths.append(3)
		else:
			x = d4/x
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))