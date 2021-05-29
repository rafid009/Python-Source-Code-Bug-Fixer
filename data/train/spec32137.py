import numpy as np 

def function(x):

	i8 = x
	f5 = 8
	paths = []
	try:
		if f5 >= 6:
			x = 4*x
			paths.append(1)
		else:
			x = 9+8
			f5 = 1-f5
			i8 = 2*i8
			paths.append(2)
		if x > 3:
			f5 = 1*8
			paths.append(3)
		else:
			f5 = f5+9
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