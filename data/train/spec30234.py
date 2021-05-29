import numpy as np 

def function(x):

	i2 = 1
	l2 = 8
	paths = []
	try:
		if x < 1:
			x = 6*x
			paths.append(1)
		else:
			x = 3*4
			l2 = l2+3
			paths.append(2)
		if l2 < 7:
			l2 = 7+l2
			l2 = l2*3
			paths.append(3)
		else:
			i2 = 1/i2
			l2 = l2+9
			l2 = l2*5
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