import numpy as np 

def function(x):

	d4 = x
	d9 = x
	paths = []
	try:
		if x > 7:
			x = 2/x
			x = 0-d9
			x = 6*x
			paths.append(1)
		else:
			d9 = x*8
			paths.append(2)
		if d9 < 6:
			d4 = d4*5
			d9 = d9*d9
			d9 = x/6
			paths.append(3)
		else:
			d4 = x*3
			d9 = 8+2
			d9 = d9-d9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))