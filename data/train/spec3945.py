import numpy as np 

def function(x):

	i2 = x
	d4 = x
	paths = []
	try:
		if d4 > 4:
			d4 = d4/8
			paths.append(1)
		else:
			x = i2+3
			d4 = 6+d4
			i2 = 8-9
			paths.append(2)
		if d4 >= 5:
			d4 = d4/i2
			paths.append(3)
		else:
			x = 9*7
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))