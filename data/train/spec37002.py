import numpy as np 

def function(x):

	a4 = x
	d9 = x
	paths = []
	try:
		if d9 > 8:
			x = x/2
			a4 = a4-x
			paths.append(1)
		else:
			x = 9-x
			a4 = 7/a4
			a4 = a4*0
			paths.append(2)
		if a4 > 9:
			x = 9/x
			d9 = 6/d9
			x = x-d9
			paths.append(3)
		else:
			a4 = 6*d9
			d9 = 4-d9
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