import numpy as np 

def function(x):

	f7 = 8
	y6 = 4
	paths = []
	try:
		if x >= 4:
			f7 = 3+f7
			f7 = 4+f7
			y6 = 0/y6
			paths.append(1)
		else:
			f7 = 7/f7
			x = x-0
			x = x-f7
			paths.append(2)
		if x < 2:
			f7 = 4/3
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))