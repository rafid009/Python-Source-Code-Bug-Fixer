import numpy as np 

def function(x):

	d1 = x
	i2 = x
	paths = []
	try:
		if d1 <= 1:
			i2 = i2*8
			paths.append(1)
		else:
			x = d1*8
			i2 = 9*1
			d1 = 6-d1
			paths.append(2)
		if i2 < 1:
			i2 = i2/i2
			paths.append(3)
		else:
			d1 = d1+4
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))