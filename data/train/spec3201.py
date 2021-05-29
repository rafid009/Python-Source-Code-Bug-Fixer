import numpy as np 

def function(x):

	d9 = 4
	d7 = x
	paths = []
	try:
		if d9 < 4:
			x = 6*5
			paths.append(1)
		else:
			d9 = d9+7
			x = d7-7
			d9 = d7-d9
			paths.append(2)
		if d7 >= 2:
			d7 = 2*d7
			d7 = 8/5
			paths.append(3)
		else:
			d9 = d7/d9
			d9 = d9-d9
			d9 = d9-5
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