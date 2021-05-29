import numpy as np 

def function(x):

	i2 = 1
	t0 = 4
	paths = []
	try:
		if i2 > 3:
			x = 5+i2
			i2 = x-i2
			paths.append(1)
		else:
			i2 = i2/t0
			x = x*2
			x = i2/x
			paths.append(2)
		if t0 > 1:
			x = i2*x
			i2 = x/6
			paths.append(3)
		else:
			x = 2/x
			x = i2+3
			x = 5/2
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