import numpy as np 

def function(x):

	d9 = 3
	d6 = 1
	x = 5
	paths = []
	try:
		if d9 >= 9:
			d6 = d6-d6
			d6 = 8-d6
			d9 = 4/d9
			paths.append(1)
		else:
			x = x-4
			x = x+5
			paths.append(2)
		if x >= 0:
			d6 = 4*d6
			d9 = 0+5
			d6 = d6-8
			paths.append(3)
		else:
			x = x+2
			d6 = d6/d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d9 = d6**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))