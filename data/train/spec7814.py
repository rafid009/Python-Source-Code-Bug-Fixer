import numpy as np 

def function(x):

	b5 = 3
	i2 = 2
	x = 1
	paths = []
	try:
		if i2 > 3:
			b5 = 6/b5
			x = 5*x
			i2 = i2+1
			paths.append(1)
		else:
			x = b5-b5
			paths.append(2)
		if x <= 9:
			x = x-1
			paths.append(3)
		else:
			b5 = b5-9
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