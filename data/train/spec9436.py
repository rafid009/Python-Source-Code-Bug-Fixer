import numpy as np 

def function(x):

	x0 = x
	i2 = 2
	paths = []
	try:
		if i2 < 3:
			x = x+9
			i2 = x*i2
			paths.append(1)
		else:
			x = 2+x0
			paths.append(2)
		if x0 < 1:
			x0 = x0-1
			x0 = x0*7
			x = 2/i2
			paths.append(3)
		else:
			x = 5-x
			i2 = i2+i2
			x = 9-4
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))