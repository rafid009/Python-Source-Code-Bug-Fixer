import numpy as np 

def function(x):

	l6 = 7
	i2 = 2
	paths = []
	try:
		if x < 0:
			i2 = i2-4
			paths.append(1)
		else:
			x = l6/x
			x = i2*x
			paths.append(2)
		if x > 7:
			x = x+l6
			l6 = 0+3
			l6 = l6-i2
			paths.append(3)
		else:
			i2 = 6/i2
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))