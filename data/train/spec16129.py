import numpy as np 

def function(x):

	v9 = 0
	d2 = 0
	paths = []
	try:
		if x < 1:
			x = x/4
			x = x/7
			paths.append(1)
		else:
			d2 = x-d2
			v9 = 5+v9
			v9 = v9-1
			paths.append(2)
		if v9 >= 7:
			x = 5-x
			paths.append(3)
		else:
			d2 = v9-d2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))