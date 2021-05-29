import numpy as np 

def function(x):

	d5 = x
	n0 = 7
	x = x
	paths = []
	try:
		if d5 <= 7:
			x = 4+5
			paths.append(1)
		else:
			d5 = 9/7
			paths.append(2)
		if d5 <= 4:
			x = n0*n0
			d5 = d5+d5
			paths.append(3)
		else:
			d5 = d5-d5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))