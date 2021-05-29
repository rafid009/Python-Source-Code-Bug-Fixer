import numpy as np 

def function(x):

	d9 = x
	i2 = x
	paths = []
	try:
		if d9 <= 8:
			i2 = i2-i2
			i2 = 6*6
			paths.append(1)
		else:
			x = x-i2
			d9 = 0/d9
			paths.append(2)
		if d9 <= 7:
			x = 7*x
			x = x+6
			paths.append(3)
		else:
			d9 = x/3
			i2 = i2/4
			x = x-5
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