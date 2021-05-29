import numpy as np 

def function(x):

	d7 = 7
	k5 = 8
	paths = []
	try:
		if k5 < 9:
			d7 = 4+9
			d7 = d7-7
			paths.append(1)
		else:
			k5 = k5+x
			paths.append(2)
		if k5 < 5:
			k5 = k5-x
			d7 = 9/d7
			k5 = 5+k5
			paths.append(3)
		else:
			d7 = 7/d7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))