import numpy as np 

def function(x):

	f5 = 1
	x4 = 6
	paths = []
	try:
		if x <= 6:
			f5 = f5*4
			x = x+3
			x4 = x4-6
			paths.append(1)
		else:
			x4 = 4-x4
			f5 = f5/1
			paths.append(2)
		if x <= 2:
			x = x*7
			x4 = x4*2
			paths.append(3)
		else:
			x = x4*x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))