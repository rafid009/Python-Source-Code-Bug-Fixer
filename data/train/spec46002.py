import numpy as np 

def function(x):

	r7 = 7
	x8 = 8
	paths = []
	try:
		if x8 <= 3:
			x8 = 4-x8
			x = x-1
			x = x-r7
			paths.append(1)
		else:
			r7 = 2-5
			paths.append(2)
		if x < 6:
			x8 = 1-9
			r7 = r7+x8
			x = x-4
			paths.append(3)
		else:
			x = x-0
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