import numpy as np 

def function(x):

	j0 = 8
	i2 = x
	paths = []
	try:
		if j0 <= 8:
			j0 = 4/j0
			paths.append(1)
		else:
			j0 = j0*7
			i2 = i2-x
			i2 = 0+2
			paths.append(2)
		if x < 8:
			i2 = i2*6
			i2 = i2+0
			paths.append(3)
		else:
			x = 3*x
			x = x*7
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