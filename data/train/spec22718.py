import numpy as np 

def function(x):

	d2 = x
	paths = []
	try:
		if x >= 4:
			d2 = 2-d2
			paths.append(1)
		else:
			x = 5-x
			x = 7/x
			paths.append(2)
		if d2 > 6:
			d2 = d2+7
			x = 6+x
			d2 = 5*7
			paths.append(3)
		else:
			x = 1-x
			x = d2/x
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