import numpy as np 

def function(x):

	x2 = x
	v7 = x
	paths = []
	try:
		if v7 < 9:
			x2 = 7+5
			v7 = v7-4
			v7 = 8/v7
			paths.append(1)
		else:
			v7 = v7/4
			x = v7-x2
			v7 = 8*1
			paths.append(2)
		if x >= 4:
			x = x-9
			x = x+8
			v7 = v7-x2
			paths.append(3)
		else:
			x2 = 7-x2
			x2 = 7/6
			x2 = x2+5
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