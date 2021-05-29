import numpy as np 

def function(x):

	i2 = x
	a6 = 2
	paths = []
	try:
		if a6 <= 6:
			i2 = i2/3
			i2 = 4*i2
			a6 = a6+1
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if i2 >= 2:
			x = i2/x
			paths.append(3)
		else:
			a6 = 3*7
			a6 = 8-a6
			i2 = 0/1
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