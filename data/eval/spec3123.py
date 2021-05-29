import numpy as np 

def function(x):

	y5 = 9
	b9 = 7
	paths = []
	try:
		if x <= 9:
			x = x+5
			y5 = b9+y5
			paths.append(1)
		else:
			b9 = b9*9
			paths.append(2)
		if x >= 6:
			b9 = b9*1
			paths.append(3)
		else:
			b9 = 9-4
			y5 = x+y5
			y5 = y5+y5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))