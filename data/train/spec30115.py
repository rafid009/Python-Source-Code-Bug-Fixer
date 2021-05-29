import numpy as np 

def function(x):

	x9 = 1
	f0 = 5
	paths = []
	try:
		if x < 9:
			x9 = 3-8
			paths.append(1)
		else:
			x = x-0
			f0 = 8-f0
			paths.append(2)
		if x > 2:
			x9 = x9*1
			f0 = 9+f0
			paths.append(3)
		else:
			f0 = f0/5
			f0 = f0+f0
			x = 8*x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))