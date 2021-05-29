import numpy as np 

def function(x):

	d2 = 4
	v9 = x
	x = 1
	paths = []
	try:
		if x < 6:
			v9 = v9*9
			paths.append(1)
		else:
			d2 = d2/6
			d2 = x/d2
			paths.append(2)
		if d2 >= 3:
			x = x-6
			x = d2/d2
			d2 = 8*v9
			paths.append(3)
		else:
			x = 1+3
			d2 = 3-v9
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