import numpy as np 

def function(x):

	i2 = 3
	y3 = 9
	x = x
	paths = []
	try:
		if x > 9:
			y3 = y3*i2
			x = 4*x
			x = x-y3
			paths.append(1)
		else:
			i2 = y3*1
			x = x/3
			paths.append(2)
		if i2 > 3:
			y3 = 5-y3
			paths.append(3)
		else:
			i2 = 0+x
			i2 = y3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))