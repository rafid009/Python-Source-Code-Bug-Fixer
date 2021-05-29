import numpy as np 

def function(x):

	d2 = x
	r3 = 2
	x = 5
	paths = []
	try:
		if d2 > 2:
			x = x-x
			x = 4+x
			paths.append(1)
		else:
			r3 = d2-3
			x = x/7
			paths.append(2)
		if d2 < 0:
			x = x-7
			d2 = 1-x
			paths.append(3)
		else:
			d2 = x-d2
			r3 = r3-0
			r3 = r3*d2
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