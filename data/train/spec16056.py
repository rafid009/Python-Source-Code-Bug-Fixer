import numpy as np 

def function(x):

	i2 = x
	o9 = x
	paths = []
	try:
		if o9 < 6:
			x = x-i2
			x = x/i2
			paths.append(1)
		else:
			i2 = 6/6
			paths.append(2)
		if i2 >= 8:
			i2 = i2/5
			x = x*x
			paths.append(3)
		else:
			x = 5+o9
			i2 = i2*6
			o9 = 1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))