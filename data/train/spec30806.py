import numpy as np 

def function(x):

	a4 = x
	i2 = 8
	paths = []
	try:
		if x > 6:
			x = 3-x
			i2 = i2/3
			x = a4+x
			paths.append(1)
		else:
			a4 = 4-a4
			paths.append(2)
		if a4 >= 5:
			i2 = a4+8
			a4 = x*4
			a4 = 8*a4
			paths.append(3)
		else:
			i2 = 6/x
			i2 = 2*i2
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))