import numpy as np 

def function(x):

	y5 = x
	i9 = 1
	paths = []
	try:
		if x < 3:
			i9 = i9/2
			paths.append(1)
		else:
			i9 = 0/3
			x = 2+6
			i9 = 2+7
			paths.append(2)
		if i9 > 6:
			x = 2*9
			i9 = 0+0
			paths.append(3)
		else:
			x = x/8
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