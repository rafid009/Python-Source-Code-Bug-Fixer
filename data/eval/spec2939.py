import numpy as np 

def function(x):

	i2 = 8
	e9 = 8
	paths = []
	try:
		if i2 <= 7:
			x = 8-e9
			paths.append(1)
		else:
			e9 = e9*2
			i2 = i2*9
			paths.append(2)
		if x < 2:
			i2 = x/x
			paths.append(3)
		else:
			i2 = i2+x
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