import numpy as np 

def function(x):

	i2 = x
	d9 = 9
	x = x
	paths = []
	try:
		if x > 9:
			x = x/x
			paths.append(1)
		else:
			d9 = 7-d9
			x = x+x
			paths.append(2)
		if i2 > 8:
			d9 = d9+5
			i2 = 4+i2
			paths.append(3)
		else:
			i2 = 6-2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))