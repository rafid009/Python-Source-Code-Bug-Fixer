import numpy as np 

def function(x):

	x6 = 6
	x7 = x
	paths = []
	try:
		if x >= 7:
			x6 = x6+9
			x6 = x6-4
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x6 <= 1:
			x6 = x6-1
			x7 = 2/x7
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))