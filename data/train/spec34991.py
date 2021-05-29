import numpy as np 

def function(x):

	w7 = x
	d4 = 4
	paths = []
	try:
		if d4 >= 3:
			w7 = d4/w7
			d4 = d4+d4
			w7 = 4/w7
			paths.append(1)
		else:
			x = 1*8
			paths.append(2)
		if x >= 1:
			d4 = d4*7
			paths.append(3)
		else:
			d4 = w7*2
			d4 = d4-3
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