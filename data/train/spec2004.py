import numpy as np 

def function(x):

	i6 = x
	y8 = 9
	paths = []
	try:
		if i6 >= 9:
			y8 = y8*y8
			x = x-4
			paths.append(1)
		else:
			y8 = y8*x
			paths.append(2)
		if x <= 6:
			x = x+x
			x = i6+x
			paths.append(3)
		else:
			y8 = 4-i6
			i6 = 0*i6
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