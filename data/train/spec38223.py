import numpy as np 

def function(x):

	x3 = x
	f5 = 9
	x = x
	paths = []
	try:
		if f5 <= 8:
			x3 = 1+x3
			paths.append(1)
		else:
			x3 = 2-9
			f5 = 8*f5
			paths.append(2)
		if x > 6:
			x = x3*x
			paths.append(3)
		else:
			x = x*9
			f5 = 2-f5
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))