import numpy as np 

def function(x):

	w8 = 5
	i2 = 4
	paths = []
	try:
		if i2 <= 6:
			w8 = w8/2
			x = x*1
			i2 = w8-x
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if i2 < 4:
			i2 = 4-i2
			i2 = x/x
			w8 = 0+w8
			paths.append(3)
		else:
			w8 = x/w8
			i2 = 8+x
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