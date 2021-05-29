import numpy as np 

def function(x):

	a8 = x
	d9 = 2
	paths = []
	try:
		if a8 < 8:
			a8 = 9*a8
			paths.append(1)
		else:
			d9 = 6-8
			x = x/9
			paths.append(2)
		if x < 9:
			x = d9*d9
			paths.append(3)
		else:
			x = 6-5
			x = x-x
			d9 = d9*d9
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