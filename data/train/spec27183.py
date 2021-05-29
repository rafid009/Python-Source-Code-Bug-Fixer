import numpy as np 

def function(x):

	f7 = x
	x7 = x
	paths = []
	try:
		if x7 < 0:
			x7 = x-0
			paths.append(1)
		else:
			f7 = f7/4
			paths.append(2)
		if x < 6:
			x = x+f7
			f7 = f7*2
			f7 = f7-6
			paths.append(3)
		else:
			x = x-5
			x = x7-x7
			x7 = 0/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))