import numpy as np 

def function(x):

	d2 = x
	v7 = 5
	paths = []
	try:
		if x > 6:
			d2 = d2-3
			paths.append(1)
		else:
			d2 = d2*6
			v7 = v7-7
			paths.append(2)
		if v7 >= 5:
			d2 = 7-v7
			v7 = v7+4
			x = 8-x
			paths.append(3)
		else:
			d2 = d2*2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))