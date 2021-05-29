import numpy as np 

def function(x):

	r9 = 1
	d2 = x
	paths = []
	try:
		if r9 > 3:
			d2 = d2+9
			r9 = x+r9
			paths.append(1)
		else:
			r9 = 9/4
			r9 = 2/6
			paths.append(2)
		if x >= 8:
			d2 = d2*8
			d2 = 2*d2
			d2 = d2+7
			paths.append(3)
		else:
			x = x-3
			d2 = d2/x
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