import numpy as np 

def function(x):

	x7 = x
	i9 = x
	paths = []
	try:
		if x < 0:
			x7 = x7+i9
			paths.append(1)
		else:
			x = x/8
			x = 3*x
			paths.append(2)
		if x7 > 7:
			x = 4+7
			x = 6*x
			paths.append(3)
		else:
			i9 = i9*3
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))