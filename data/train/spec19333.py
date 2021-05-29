import numpy as np 

def function(x):

	d9 = x
	i6 = 6
	paths = []
	try:
		if i6 >= 7:
			d9 = x-1
			paths.append(1)
		else:
			i6 = d9-9
			i6 = d9+0
			paths.append(2)
		if d9 > 6:
			i6 = 5-i6
			paths.append(3)
		else:
			d9 = 6*d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))