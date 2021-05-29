import numpy as np 

def function(x):

	a5 = x
	i2 = 7
	paths = []
	try:
		if i2 < 2:
			x = i2-x
			x = x-a5
			paths.append(1)
		else:
			i2 = 8*i2
			paths.append(2)
		if a5 >= 3:
			i2 = 1*i2
			a5 = 9-0
			i2 = 6/4
			paths.append(3)
		else:
			a5 = 1/a5
			x = x-9
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))