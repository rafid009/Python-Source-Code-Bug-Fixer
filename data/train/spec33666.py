import numpy as np 

def function(x):

	i2 = x
	y2 = x
	paths = []
	try:
		if x >= 5:
			x = i2+5
			paths.append(1)
		else:
			x = 6*x
			y2 = i2+y2
			x = 8+1
			paths.append(2)
		if i2 > 5:
			x = 8/2
			i2 = 0+2
			i2 = 0*y2
			paths.append(3)
		else:
			x = y2/i2
			x = y2*x
			x = x/4
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