import numpy as np 

def function(x):

	d2 = x
	i2 = x
	paths = []
	try:
		if x <= 7:
			x = x/3
			x = x*i2
			i2 = d2-x
			paths.append(1)
		else:
			x = 5-2
			paths.append(2)
		if d2 < 5:
			i2 = 2-i2
			paths.append(3)
		else:
			i2 = d2*i2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))