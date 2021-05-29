import numpy as np 

def function(x):

	d5 = x
	j1 = x
	paths = []
	try:
		if x >= 3:
			d5 = 1*d5
			paths.append(1)
		else:
			x = 2/1
			x = d5/6
			paths.append(2)
		if d5 > 3:
			x = d5-2
			paths.append(3)
		else:
			x = x-x
			j1 = 7-j1
			x = x-8
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))