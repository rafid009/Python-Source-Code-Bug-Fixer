import numpy as np 

def function(x):

	x7 = x
	b8 = 9
	paths = []
	try:
		if b8 < 9:
			b8 = 9-x
			x7 = x/3
			paths.append(1)
		else:
			x7 = 8+x
			x7 = x7/x7
			paths.append(2)
		if x7 > 2:
			x = 4+7
			paths.append(3)
		else:
			x7 = 8/x7
			x7 = x+x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		b8 = x7**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))