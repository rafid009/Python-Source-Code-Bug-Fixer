import numpy as np 

def function(x):

	i7 = 1
	x6 = x
	paths = []
	try:
		if x >= 3:
			x6 = x6*x6
			paths.append(1)
		else:
			x6 = 6/x6
			paths.append(2)
		if i7 < 8:
			x = 6/x
			paths.append(3)
		else:
			x = 7*2
			x = 8*x
			x6 = x6+7
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))