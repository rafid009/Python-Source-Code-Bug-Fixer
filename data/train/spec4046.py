import numpy as np 

def function(x):

	i2 = 1
	a6 = 5
	paths = []
	try:
		if x >= 3:
			a6 = 0-a6
			i2 = 4-6
			a6 = a6/a6
			paths.append(1)
		else:
			a6 = x*x
			i2 = i2*i2
			i2 = i2*3
			paths.append(2)
		if x > 6:
			x = i2-x
			paths.append(3)
		else:
			i2 = i2+0
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