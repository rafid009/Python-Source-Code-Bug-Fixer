import numpy as np 

def function(x):

	l7 = x
	i2 = x
	paths = []
	try:
		if x >= 0:
			x = x-x
			paths.append(1)
		else:
			x = 1/8
			i2 = 8+i2
			x = 2-x
			paths.append(2)
		if i2 > 2:
			i2 = 0/8
			paths.append(3)
		else:
			x = i2*x
			l7 = l7/4
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		i2 = l7**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))