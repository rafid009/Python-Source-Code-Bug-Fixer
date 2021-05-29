import numpy as np 

def function(x):

	d2 = 0
	d1 = 0
	paths = []
	try:
		if d2 > 6:
			d2 = d2/d1
			paths.append(1)
		else:
			d1 = x-d1
			d2 = x+9
			paths.append(2)
		if d1 >= 8:
			d2 = 2/d2
			paths.append(3)
		else:
			x = d2*x
			d2 = d2+7
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))