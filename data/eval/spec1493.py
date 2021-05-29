import numpy as np 

def function(x):

	i2 = x
	a5 = 4
	paths = []
	try:
		if a5 >= 7:
			x = 4/x
			paths.append(1)
		else:
			x = x+i2
			a5 = a5-1
			i2 = 6/9
			paths.append(2)
		if i2 <= 8:
			x = 1*x
			a5 = 8-6
			i2 = i2-8
			paths.append(3)
		else:
			x = 6*x
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