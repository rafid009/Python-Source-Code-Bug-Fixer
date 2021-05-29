import numpy as np 

def function(x):

	d9 = x
	q0 = 0
	paths = []
	try:
		if d9 < 6:
			d9 = d9-3
			x = 0+x
			paths.append(1)
		else:
			x = 6+8
			q0 = 4-q0
			paths.append(2)
		if q0 >= 9:
			d9 = 1-d9
			q0 = 9+3
			paths.append(3)
		else:
			q0 = 4+5
			d9 = d9+0
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))