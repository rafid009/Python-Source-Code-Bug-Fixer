import numpy as np 

def function(x):

	x3 = 8
	f8 = x
	paths = []
	try:
		if x > 5:
			x3 = 8/8
			paths.append(1)
		else:
			x3 = x3+x
			f8 = f8-3
			paths.append(2)
		if f8 >= 3:
			x3 = 3*x
			x3 = 2+x
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))