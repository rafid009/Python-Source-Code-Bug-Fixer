import numpy as np 

def function(x):

	f0 = x
	y8 = 6
	paths = []
	try:
		if f0 < 9:
			f0 = f0+1
			y8 = y8-1
			f0 = f0/y8
			paths.append(1)
		else:
			x = f0-y8
			paths.append(2)
		if f0 > 0:
			f0 = 1+y8
			x = f0+5
			paths.append(3)
		else:
			x = f0/1
			y8 = 3+f0
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))