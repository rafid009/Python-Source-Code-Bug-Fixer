import numpy as np 

def function(x):

	i2 = x
	y1 = 5
	paths = []
	try:
		if i2 > 3:
			y1 = x*7
			i2 = i2-i2
			x = x/x
			paths.append(1)
		else:
			x = 9*x
			x = x+2
			paths.append(2)
		if i2 < 2:
			x = 0/x
			paths.append(3)
		else:
			i2 = 2*4
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		y1 = i2**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))