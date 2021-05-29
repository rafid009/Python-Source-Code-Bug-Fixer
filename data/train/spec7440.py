import numpy as np 

def function(x):

	d4 = x
	y8 = 4
	paths = []
	try:
		if x <= 9:
			y8 = 9/y8
			y8 = 4-y8
			x = 5*x
			paths.append(1)
		else:
			y8 = d4*5
			y8 = 7-d4
			d4 = d4/d4
			paths.append(2)
		if y8 > 3:
			d4 = d4+1
			paths.append(3)
		else:
			d4 = 7*d4
			x = x/y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		d4 = y8**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))