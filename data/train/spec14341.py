import numpy as np 

def function(x):

	x8 = x
	e3 = 7
	paths = []
	try:
		if x >= 3:
			e3 = e3+1
			paths.append(1)
		else:
			x = x-3
			x8 = x8-1
			paths.append(2)
		if x < 8:
			x8 = 8*x
			x = e3*5
			x8 = x8*1
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))