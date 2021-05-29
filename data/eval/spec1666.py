import numpy as np 

def function(x):

	d1 = 5
	i2 = x
	paths = []
	try:
		if x < 7:
			d1 = 6-d1
			paths.append(1)
		else:
			i2 = 4*i2
			paths.append(2)
		if d1 > 7:
			i2 = 0/3
			x = 2+1
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))